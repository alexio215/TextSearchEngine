import json
import re
import typing
from pathlib import Path
from typing import List


class TranscriptUtterance(typing.NamedTuple):
    source_name: str
    index: int
    time: str
    speaker: str
    text: str


LECTURES_DIR = r'C:\Users\Alex\Documents\DePaul\csc299-winter2023\lectures'
TRANSCRIPT_FNAME_SUFFIX = '.transcript.vtt'


def get_source_paths():
    root = Path(LECTURES_DIR)
    relative_paths = root.glob('**/*' + TRANSCRIPT_FNAME_SUFFIX)
    return [root / path for path in relative_paths]


DATA_DIR = r'C:\Users\Alex\Documents\DePaul\csc299-winter2023\datasets\lecture_transcripts'


def write_records_to_json(
        name: str, records: List[List[TranscriptUtterance]]) -> None:
    out_path = Path(DATA_DIR) / Path(name + '.json')
    with out_path.open('w') as fp:
        json.dump(obj=[r._asdict() for rr in records for r in rr], fp=fp)


def write_records_to_jsonl(
        name: str, records: List[List[TranscriptUtterance]]) -> None:
    out_path = Path(DATA_DIR) / Path(name + '.jsonl')
    with out_path.open('w') as fp:
        for r_list in records:
            for r in r_list:
                fp.write(json.dumps(r._asdict()) + '\n')


def read_records(source_paths: List[Path]) -> List[List[TranscriptUtterance]]:
    # source_paths = get_source_paths()
    out = []
    for source_path in source_paths:
        utterances = []
        index: int = None
        time: str = None
        speaker: str = None
        text: str = None

        with source_path.open() as fp:
            update_count = 0
            for l in fp:
                if re.match(r'\d+\s*$', l):
                    index = int(l)
                    update_count += 1
                elif re.match(r'[\d:.]+ --> [\d:.]+\s*$', l):
                    time = l.strip()
                    update_count += 1
                elif re.match(r'(.*?):\s*(.*)\s*$', l):
                    m = re.match(r'(.*?):\s*(.*)\s*$', l)
                    speaker, text = m.group(1, 2)
                    update_count += 1
                elif re.match(r'\s*$', l) and index is not None:
                    record = TranscriptUtterance(
                        source_name=source_path.parent.name, index=index, time=time,
                        speaker=speaker, text=text)
                    if update_count != 3:
                        print(f"Only {update_count} values updated in {record}")
                    utterances.append(record)
                    update_count = 0
                else:
                    text = l.strip()
                    update_count += 1
                    # print(f"Could not parse input string {l}")
        out.append(utterances)
    return out
