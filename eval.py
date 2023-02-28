import json
import typing

import index
import indexing_process


class QueryRecord(typing.NamedTuple):
    query_id: str
    query_text: str

def read_queries(queries_path) -> typing.List[QueryRecord]
    out = []
    with open(queries_path) as fp:
        for line in fp:
            record = json.loads(line)
            out.append(QueryRecord(query_id = record['_id'], query_text = record['metadata']['query']))
    return out

class EvalEntry(typing.NamedTuple):
    query_id: str
    doc_id: str
    score: int

class ResultScorer:
    def score_results(self, result_eval_entries: typing.List[EvalEntry]) -> float:
        pass
class TotalScoreScorer(ResultScorer):
    def score_results(self, result_eval_entries: typing.List[EvalEntry]) -> float:
        return sum(r.score for r in result_eval_entries)

class TopNScorer(ResultScorer):
    def __init__(self, n:int = 10):
        self.n = n
    def score_results(self, result_eval_entries: typing.List[EvalEntry]) -> float:
        score = 0
        query_count = 0
        last_query_id = None
        for r in result_eval_entries:
            curr_query_id = r.query_id
            if r.query_id != last_query_id:
                query_count = 0
                last_query_id = r.query_id
            if query_count < self.n:
                score += r.score
            query_count += 1
        return score

def score_results(result_eval_entries) -> float:


def read_eval_data(path: str):
    out = []
    with open(queries_path) as fp:
        for line in fp:
            record = line.split()
            out.append(EvalEntry(query_id=record[0], doc_id=record[1], score = int(record[2])))
    return out
def generate_result_eval_entires(results: typing.List[str], eval_data: typing.List[EvalEntry]) -> typing.List[EvalEntry]:
    eval_data_dict = {(entry.query_id, entry.doc_id ): entry.score for entry in eval_data}
    out = []
    for r in results:
        score = eval_data_dict.get((query_id, r), default=0)
        out.append(EvalEntry(query_id= query_id, doc_id= r, score = score))
    return out


def run_eval(index: index.Index, queries_path: str, eval_data_path: str, scorer: ResultScorer) -> float:
    query_records = read_queries(queries_path)
    eval_records = read_eval_data(eval_data_path)
    #run queries on our search engine
    tokenizer = indexing_process.NaiveTokenizer()
    result_eval_entries = []
    for query_record in query_records:
        results = index.search(tokenizer.tokenize(query_record.query_text))
        result_eval_entries.extend(generate_result_eval_entires(query_id = query_record.query_id, results = results, eval_data= eval_records))
    #compute evaluation
    return scorer.score_results(result_eval_entries)