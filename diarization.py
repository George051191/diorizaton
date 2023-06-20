from pyannote.audio import Pipeline 
import os
current_dir = os.getcwd()
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
                                    use_auth_token="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") 

# 4. apply pretrained pipeline
diarization = pipeline(current_dir + "/vosktest.wav") 
print(os.path.exists(current_dir + "/vosktest.wav"))
# 5. print the result
for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}") 


    