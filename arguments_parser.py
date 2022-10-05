import argparse
parser = argparse.ArgumentParser()    
parser.add_argument('--step',default=0.9, type = float)
parser.add_argument('--results',default=False, type = bool)
parser.add_argument('--visualize', action='store_true')
parser.add_argument('--model',default=None, type = str)
parser.add_argument('--results_path',default='../results', type = str)


args = parser.parse_args()

print(args.step)
print(args.visualize)