from paint.CanvasSwampy import CanvasSwampy
from paint.CanvasPNG import CanvasPNG

def get_canvas(canvas_type, *args, **kwargs):
    if canvas_type == "swampy":
        return CanvasSwampy(*args, **kwargs)
    elif canvas_type == "PNG":
        return CanvasPNG(*args, **kwargs)


    print(f"{canvas_type} is not supported!")
