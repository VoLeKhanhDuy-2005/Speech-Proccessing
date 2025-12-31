# import librosa
# import soundfile as sf
# import numpy as np

# def remove_silence(input_wav, output_wav, top_db=20):
#     # Load audio
#     y, sr = librosa.load(input_wav, sr=None)

#     # Detect non-silent intervals (energy-based)
#     intervals = librosa.effects.split(y, top_db=top_db)

#     # Ghép các đoạn không im lặng
#     y_trimmed = np.concatenate([y[start:end] for start, end in intervals])

#     # Save output
#     sf.write(output_wav, y_trimmed, sr)

#     return intervals

# intervals = remove_silence(
#     "Record/cat_1.wav",
#     "Record/cat_1_no_silence.wav",
#     top_db=20
# )
# print(intervals)

import os
import librosa
import soundfile as sf
import numpy as np

def remove_silence_folder(
    input_dir,
    output_dir,
    top_db=20
):
    os.makedirs(output_dir, exist_ok=True)

    results = {}

    for file in os.listdir(input_dir):
        if file.lower().endswith(".wav"):
            input_wav = os.path.join(input_dir, file)
            output_wav = os.path.join(output_dir, file)

            # Load audio
            y, sr = librosa.load(input_wav, sr=None)

            # Detect non-silent intervals
            intervals = librosa.effects.split(y, top_db=top_db)

            if len(intervals) == 0:
                print(f"[WARN] No sound detected in {file}")
                continue

            # Concatenate non-silent segments
            y_trimmed = np.concatenate(
                [y[start:end] for start, end in intervals]
            )

            # Save
            sf.write(output_wav, y_trimmed, sr)

            results[file] = intervals

            print(f"[OK] {file} → saved ({len(y_trimmed)/sr:.2f}s)")

    return results
# intervals_dict = remove_silence_folder(
#     input_dir="Record/cat",
#     output_dir="Record/Record_cat_no_silence",
#     top_db=20
# )

# intervals_dict = remove_silence_folder(
#     input_dir="Record/dog",
#     output_dir="Record/Record_dog_no_silence",
#     top_db=20
# )

# intervals_dict = remove_silence_folder(
#     input_dir="Record/test/cats",
#     output_dir="Record/Record_cat_no_silence_test",
#     top_db=20
# )

intervals_dict = remove_silence_folder(
    input_dir="Record/test/dogs",
    output_dir="Record/Record_dog_no_silence_test",
    top_db=20
)

print(intervals_dict)
