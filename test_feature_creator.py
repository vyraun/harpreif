import argparse
from rep_viz.state_indexer import Image2Feature
'''
SAMPLE RUN INSTRUCTIONS
python test_feature_extractor.py --test_images '/work/03713/harshal1/maverick/RLProj/test'
               --saved_checkpoint'/work/03713/harshal1/maverick/RLProj/checkpoint/'
               --image_feat_dir './'
               --grid_dim 8
               --num_gradients 8
'''
parser = argparse.ArgumentParser()
parser.add_argument('--test_images', type=str)
parser.add_argument('--saved_checkpoint', type=str)
parser.add_argument('--grid_dim', type=int, default=8)
parser.add_argument('--num_gradients', type=int, default=8)
parser.add_argument('image_feat_dir', type=str, default='./')
opt = parser.parse_args()


num_actions = opt.grid_dim ** 4

im2f = Image2Feature(opt.test_images, opt.saved_checkpoint, num_actions, opt.num_gradients)
image2feature_map, feat_sz = im2f.image2feature(save_transform=True, im2f_loc= opt.image_feat_dir)






