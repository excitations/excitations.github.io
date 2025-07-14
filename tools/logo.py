import typer
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Circle:
    x: float
    y: float
    r: float
    c: str = field(default_factory=lambda:'#6f6f6f')
    
    def svg(self):
        return f'<circle cx="{self.x}" cy="{self.y}" r="{self.r}" fill="{self.c}" />'
        

@dataclass
class Image:
    objs: list[Circle] = field(default_factory=list)
    
    def add(self, objs: list[Circle]):
        self.objs += objs
    
    def svg(self):
        xmin = min(c.x - c.r for c in self.objs)
        xmax = max(c.x + c.r for c in self.objs)
        ymin = min(c.y - c.r for c in self.objs)
        ymax = max(c.y + c.r for c in self.objs)
        mn = min(xmin, ymin)
        rn = max(xmax-mn, ymax-mn)
        opening = f'<svg viewBox="{mn} {mn} {rn} {rn}" xmlns="http://www.w3.org/2000/svg">'
        closing = "</svg>"
        return opening + " ".join(c.svg() for c in self.objs) + closing


def rtheta(A, B, n=10, s=5):
    from numpy import linspace, acos, hstack, vstack, unique, pi
    # find half of one:
    r = A + 2 * B * (1 - linspace(0, 1, n)**3)
    t = acos((r - A)/B - 1) / s
    # extend to the full lobe
    r = hstack((r, r[::-1]))
    t = hstack((t, 2 * pi - t[::-1]))
    # repeat s times
    r = hstack([r for _ in range(s)])
    t = hstack([2 * pi / s * n + t for n in range(s)]) % (2 * pi)
    # sort by theta and keep only unique entries
    tr = unique(vstack((t, r)).T, axis=0)
    return tr[:, 1], tr[:, 0]


def xyr(A, B, n=10, s=5, theta=0, color: str= '#000000'):
    from numpy import cos, sin, sqrt
    r, t = rtheta(A, B, n=n, s=s)
    x = r * sin(t+theta)
    y = r * cos(t+theta)
    no = len(x)
    xf = [(x[i] + x[(i+1)%no])/2 for i in range(no)]
    yf = [(y[i] + y[(i+1)%no])/2 for i in range(no)]
    xb = [(x[i] + x[(i-1)%no])/2 for i in range(no)]
    yb = [(y[i] + y[(i-1)%no])/2 for i in range(no)]
    rf = sqrt((xf-x)**2 + (yf-y)**2)
    rb = sqrt((xb-x)**2 + (yb-y)**2)
    ri = [min(f, b) for f, b in zip(rf, rb)]
    return [Circle(x, y, r, color) for x, y, r in zip(x, y, ri)]
    
    
def main(output: Path, 
         A: float=6, B: float=3, r0: float=3.5, 
         points: int=6, lobes: int=7, theta: float=0, 
         color: str = '#9f9f9f',
         ico: bool = True
         ):
    corona = xyr(A, B, n=points, s=lobes, theta=theta, color=color)
    center = Circle(0, 0, 0.9*(A - max(c.r for c in corona)), color)
    image = Image([center] + corona)
    with output.open('w') as file:
        file.write(image.svg())
    if ico:
       from subprocess import run
       from shutil import which
       if not which('magick'):
           raise RuntimeError('ImageMagick with `magick` command must be available for ICO creation')
       cmd = ['magick', '-density', '256x256', '-background', 'transparent', str(output), 
              '-define', 'icon:auto-resize', '-colors', '256', str(output.with_suffix('.ico'))]
       res = run(cmd, capture_output=True, text=True)
       if res.returncode or len(res.stderr):
           message = f'Creating ico file produced error: {res.stderr}'
           raise RuntimeError(message)
                  
        
def cli_main():
    typer.run(main)
    
if __name__ == '__main__':
    typer.run(main)


