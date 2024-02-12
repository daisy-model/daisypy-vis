'''Compare image files'''
import os
import shutil
import numpy as np
from PIL import Image

__all__ = [
    'compare_image_files',
    'compare_images',
]

def compare_image_files(dir1, dir2, filenames, error_dir, copy_on_error=True, rms_tolerance=2):
    '''Compare image files in dir1 and dir2. Combining filecmp.cmpfiles with pytest_mpl style
    comparison.

    Parameters
    ----------
    dir1 : str
      Path to directory

    dir2 : str
      Path to other directory

    filenames : sequence of str
      Sequence of filenames to compare in `dir1` and `dir2`

    error_dir : str
      Directory for images that fail to match

    copy_on_error : bool
      If True copy files that fail comparison to `error_dir`

    rms_tolerance : float
      The maximum root mean squared difference before files do not match

    Returns
    -------
    match, mismatch, error : triple of list of str
      Each filename from `filenames` is in one of the lists. It is in
      `match` if the match succeeded
      `mismatch` if the match fails
      `error` if the there is an error during the comparison.
    

    See also
    --------
    filecmp.cmpfiles
    '''
    # pylint: disable=too-many-arguments
    match, mismatch, error = [], [], []
    for fname in filenames:
        try:
            rms = compare_images(os.path.join(dir1, fname), os.path.join(dir2, fname))
            if rms <= rms_tolerance:
                match.append(fname)
            else:
                mismatch.append(fname)
        except: #pylint: disable=bare-except; We dont care which error, only that it is an error
            error.append(fname)

    if copy_on_error and (len(match) != len(filenames) or len(mismatch) == 0 or len(error) == 0):
        os.makedirs(error_dir, exist_ok=True)
        for fname in mismatch + error:
            # pylint: disable=bare-except; Try to copy, but files might not exist
            try:
                shutil.copy(os.path.join(dir1, fname),
                            os.path.join(error_dir, f'dir1_{fname}'))
            except:
                pass
            try:
                shutil.copy(os.path.join(dir2, fname),
                            os.path.join(error_dir, f'dir2_{fname}'))
            except:
                pass
    return match, mismatch, error
            
    
def compare_images(path1, path2):
    '''Compute root mean square difference of two images

    Parameters
    ----------
    path1 : str
      Path to image

    path2 : str
      Path to other image

    Returns
    -------
    rms : float
      Root mean square of difference between images
    '''
    with Image.open(path1) as im1:
        with Image.open(path2) as im2:
            im1, im2 = np.array(im1), np.array(im2)
            if im1.shape != im2.shape:
                rms = np.inf
            else:
                rms = np.sqrt(np.mean((np.array(im1) - np.array(im2))**2))
    return rms
