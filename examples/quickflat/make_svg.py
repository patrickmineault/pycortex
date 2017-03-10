"""
=====================================================
Save a 2D static flatmap using the quickflat module
=====================================================

Plot a 2D static flatmap and save it as SVG file.

**Some words on the `rechache` parameter before we begin:**

Setting the `recache=True` parameter recaches the flatmap cache located in
<filestore>/<subject>/cache. By default intermediate steps for a flatmap are
cached after the first generation to speed up the process for the future. If
any of the intermediate steps changes, the flatmap generation may fail.
`recache=True` will load these intermediate steps new.
This can be helpful if you think there is no reason that the
`quickflat.make_figure` to fail but it nevertheless fails. Try it, it's magic!

"""
import cortex

# Create a random pycortex Volume
volume = cortex.Volume.random(subject='S1', xfmname='fullhead')

# Plot a flatmap with the data projected onto the surface
_ = cortex.quickflat.make_figure(volume)

# Save this flatmap
filename = "./my_flatmap.svg"
_ = cortex.quickflat.make_png(filename, volume, recache=False)
