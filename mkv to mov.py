import subprocess

# Replace input_path and output_path with the actual paths to your files
input_path = '/path/to/input_file.mkv'
output_path = '/path/to/output_file.mov'

# Use subprocess to call the ffmpeg command-line tool
subprocess.call(['ffmpeg', '-i', input_path, '-codec', 'copy', output_path])
