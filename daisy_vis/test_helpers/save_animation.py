'''Save plotly animation'''
import os
import plotly

__all__ = [
    'save_animation'
]

def save_animation(fig, out_dir, image_format='png'):
    '''Save a plotly animation as a series of images

    Parameters
    ----------
    fig : plotly.graph_pbjects.Figure
      Figure to save

    out_dir : str
      Directory to save images to

    image_format : str
      Image format to save as

    Returns
    -------
    fnames : set of filenames that have been saved
    '''
    os.makedirs(out_dir, exist_ok=True)
    fnames = set()
    for frame in range(len(fig.frames)):
        fig.layout['sliders'][0]['active'] = frame
        fig = plotly.graph_objects.Figure(data=fig['frames'][frame]['data'],
                                          frames=fig['frames'],
                                          layout=fig.layout)
        fname = f'frame-{frame:02d}.{image_format}'
        fig.write_image(os.path.join(out_dir, fname))
        fnames.add(fname)
    return fnames
