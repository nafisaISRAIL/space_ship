def get_frames_from_files(filenames):
    frames = []
    for filename in filenames:
        with open(filename) as f:
            frames.append(f.read())
    return frames
