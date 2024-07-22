import pixellib
import tensorflow

from pixellib.tune_bg import alter_bg

change_gb = alter_bg()
change_gb.load_pascalvoc_model("deaplabv3_xception_tf_dim_ordering_tf_kernels.h5")
change_gb.color_bg("wilson.jpg", colors=(0,128,0), output_image_name=("wilson_wo_bg.jpg"))
