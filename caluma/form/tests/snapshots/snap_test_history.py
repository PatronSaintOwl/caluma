# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots["test_document_as_of 1"] = {
    "documentAsOf": {
        "historicalAnswers": {
            "edges": [
                {
                    "node": {
                        "__typename": "HistoricalStringAnswer",
                        "historyUserId": "admin",
                        "value": "first admin - revision 1",
                    }
                }
            ]
        },
        "meta": {},
    }
}

snapshots["test_document_as_of 2"] = {
    "documentAsOf": {
        "historicalAnswers": {
            "edges": [
                {
                    "node": {
                        "__typename": "HistoricalStringAnswer",
                        "historyUserId": "AnonymousUser",
                        "value": "first anon - revision 3",
                    }
                }
            ]
        },
        "meta": {},
    }
}

snapshots["test_document_as_of 3"] = {
    "documentAsOf": {
        "historicalAnswers": {
            "edges": [
                {
                    "node": {
                        "__typename": "HistoricalStringAnswer",
                        "historyUserId": "AnonymousUser",
                        "value": "second anon - revision 4",
                    }
                }
            ]
        },
        "meta": {},
    }
}

snapshots["test_historical_table_answer 1"] = {
    "d1": {
        "historicalAnswers": {
            "edges": [
                {
                    "node": {
                        "__typename": "HistoricalTableAnswer",
                        "value": [
                            {
                                "historicalAnswers": {
                                    "edges": [{"node": {"value": "first row value"}}]
                                }
                            },
                            {
                                "historicalAnswers": {
                                    "edges": [{"node": {"value": "second row value"}}]
                                }
                            },
                        ],
                    }
                }
            ]
        }
    },
    "d2": {
        "historicalAnswers": {
            "edges": [
                {
                    "node": {
                        "__typename": "HistoricalTableAnswer",
                        "value": [
                            {
                                "historicalAnswers": {
                                    "edges": [{"node": {"value": "first row value"}}]
                                }
                            }
                        ],
                    }
                }
            ]
        }
    },
}
