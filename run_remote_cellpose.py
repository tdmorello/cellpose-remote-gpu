# ssh state-cabin-cruise-dressed.trycloudflare.com -i ~/.ssh/colab-cellpose

from argparse import ArgumentParser
import subprocess
import shlex
from pathlib import Path

parser = ArgumentParser(
    description="Download Google Drive folder to local")
parser.add_argument('-d', '--directory', type=Path,
                    help='a folder containing tiff files')
parser.add_argument('-a', '--ssh-address', type=str,
                    help='Generated ssh address')
parser.add_argument('-i', '--identity', type=str,
                    help='Local private identity file')
parser.add_argument('--min', type=float,
                    help='minimum normalization value')
parser.add_argument('--max', type=float,
                    help='max normalization value')
parser.add_argument('--diameter', type=float,
                    help='average cell/nucleus diameter. Highly recommended to set for speed reasons')
parser.add_argument('--net_avg', type=bool,
                    help='runs the 4 built-in networks and averages them if True, runs one network if False')
parser.add_argument('--ch_cyto', type=int,
                    help='cyto channel number')
parser.add_argument('--ch_nuc', type=int,
                    help='nuc channel number')
parser.add_argument('--model', type=str,
                    help='cellpose model name')

args = parser.parse_args()
ssh_address = args.ssh_address
image_folder = args.directory
net_avg = True
diameter = args.diameter  # If diameter is None, CellPose will try to estimate it. Slow
ch_cyto = args.ch_cyto
ch_nuc = args.ch_nuc
model = args.model
min = args.min
max = args.max


def run_command(command):
    print('running ', command)
    args = shlex.split(command)
    stdout, stderr = subprocess.Popen(args,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE
                                      ).communicate()

    stdout, stderr = stdout.decode(), stderr.decode()
    return stdout, stderr


identity_file = '/Users/tim/.ssh/colab-cellpose'
src_path = Path('/Users/tim/Research/Data-Analysis/remote-gpu-cellpose/remote-scripts/remote_cellpose_script.py')
remote_script_path = f'/content/{src_path.name}'
# ssh_address = 'root-probability-java-earn.trycloudflare.com'

command = f"scp -o 'StrictHostKeyChecking no' -i '{identity_file}' {src_path.absolute()} {ssh_address}:{remote_script_path}"
stdout, stderr = run_command(command)
print(stdout)
print(stderr)

command = f"ssh -i {identity_file} {ssh_address} 'python3 {remote_script_path} {image_folder} --min {min} --max {max} --diameter {diameter} --net_avg {net_avg} --ch_cyto {ch_cyto} --ch_nuc {ch_nuc} --model {model}'"
stdout, stderr = run_command(command)
print(stdout)
print(stderr)
