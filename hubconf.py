dependencies = ['torch', 'torchaudio']
import torch
from utils_vad import (init_jit_model,
                       get_speech_ts,
                       get_speech_ts_adaptive,
                       get_number_ts,
                       get_language,
                       save_audio,
                       read_audio,
                       state_generator,
                       single_audio_stream,
                       collect_chunks,
                       drop_chunks)


def silero_vad(**kwargs):
    """Silero Voice Activity Detector
    Returns a model with a set of utils
    Please see https://github.com/snakers4/silero-vad for usage examples
    """
    hub_dir = torch.hub.get_dir()
    model = init_jit_model(model_path=f'{hub_dir}/snakers4_silero-vad_master/files/model.jit')
    utils = (get_speech_ts,
             get_speech_ts_adaptive,
             save_audio,
             read_audio,
             state_generator,
             single_audio_stream,
             collect_chunks)

    return model, utils


def silero_vad_micro(**kwargs):
    """Silero Voice Activity Detector
    Returns a model with a set of utils
    Please see https://github.com/snakers4/silero-vad for usage examples
    """
    hub_dir = torch.hub.get_dir()
    model = init_jit_model(model_path=f'{hub_dir}/snakers4_silero-vad_master/files/model_micro.jit')
    utils = (get_speech_ts,
             get_speech_ts_adaptive,
             save_audio,
             read_audio,
             state_generator,
             single_audio_stream,
             collect_chunks)

    return model, utils


def silero_vad_micro_8k(**kwargs):
    """Silero Voice Activity Detector
    Returns a model with a set of utils
    Please see https://github.com/snakers4/silero-vad for usage examples
    """
    hub_dir = torch.hub.get_dir()
    model = init_jit_model(model_path=f'{hub_dir}/snakers4_silero-vad_master/files/model_micro_8k.jit')
    utils = (get_speech_ts,
             get_speech_ts_adaptive,
             save_audio,
             read_audio,
             state_generator,
             single_audio_stream,
             collect_chunks)

    return model, utils


def silero_vad_mini(**kwargs):
    """Silero Voice Activity Detector
    Returns a model with a set of utils
    Please see https://github.com/snakers4/silero-vad for usage examples
    """
    hub_dir = torch.hub.get_dir()
    model = init_jit_model(model_path=f'{hub_dir}/snakers4_silero-vad_master/files/model_mini.jit')
    utils = (get_speech_ts,
             get_speech_ts_adaptive,
             save_audio,
             read_audio,
             state_generator,
             single_audio_stream,
             collect_chunks)

    return model, utils


def silero_vad_mini_8k(**kwargs):
    """Silero Voice Activity Detector
    Returns a model with a set of utils
    Please see https://github.com/snakers4/silero-vad for usage examples
    """
    hub_dir = torch.hub.get_dir()
    model = init_jit_model(model_path=f'{hub_dir}/snakers4_silero-vad_master/files/model_mini_8k.jit')
    utils = (get_speech_ts,
             get_speech_ts_adaptive,
             save_audio,
             read_audio,
             state_generator,
             single_audio_stream,
             collect_chunks)

    return model, utils


def silero_number_detector(**kwargs):
    """Silero Number Detector
    Returns a model with a set of utils
    Please see https://github.com/snakers4/silero-vad for usage examples
    """
    hub_dir = torch.hub.get_dir()
    model = init_jit_model(model_path=f'{hub_dir}/snakers4_silero-vad_master/files/number_detector.jit')
    utils = (get_number_ts,
             save_audio,
             read_audio,
             collect_chunks,
             drop_chunks)

    return model, utils


def silero_lang_detector(**kwargs):
    """Silero Language Classifier
    Returns a model with a set of utils
    Please see https://github.com/snakers4/silero-vad for usage examples
    """
    hub_dir = torch.hub.get_dir()
    model = init_jit_model(model_path=f'{hub_dir}/snakers4_silero-vad_master/files/number_detector.jit')
    utils = (get_language,
             read_audio)

    return model, utils
