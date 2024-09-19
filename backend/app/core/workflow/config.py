config_with_2_tool_router = {
    "id": "26f834ee-b8cd-46ad-b655-fd20ba27d8ba",
    "name": "Flow Visualization",
    "nodes": [
        {
            "id": "start-1",
            "type": "start",
            "position": {"x": 88, "y": 172},
            "data": {"label": "Start"},
        },
        {
            "id": "llm-2",
            "type": "llm",
            "position": {"x": 452, "y": 182},
            "data": {
                "label": "LLM",
                "model": "glm-4",
                "temperature": 0.7,
            },
        },
        {
            "id": "tool-3",
            "type": "tool",
            "position": {"x": 766, "y": 484},
            "data": {"label": "Tool", "tools": ["calculator"]},
        },
        {
            "id": "tool-4",
            "type": "tool",
            "position": {"x": 847, "y": 116},
            "data": {"label": "Tool", "tools": ["tavilysearch"]},
        },
        {
            "id": "end-5",
            "type": "end",
            "position": {"x": 1216, "y": 287},
            "data": {"label": "End"},
        },
    ],
    "edges": [
        {
            "id": "reactflow__edge-start-1right-llm-2left",
            "source": "start-1",
            "target": "llm-2",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "default",
        },
        {
            "id": "reactflow__edge-llm-2right-tool-3left",
            "source": "llm-2",
            "target": "tool-3",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "smoothstep",
        },
        {
            "id": "reactflow__edge-llm-2right-tool-4left",
            "source": "llm-2",
            "target": "tool-4",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "smoothstep",
        },
        {
            "id": "reactflow__edge-llm-2right-end-5left",
            "source": "llm-2",
            "target": "end-5",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "smoothstep",
        },
        {
            "id": "reactflow__edge-tool-3right-llm-2right",
            "source": "tool-3",
            "target": "llm-2",
            "sourceHandle": "right",
            "targetHandle": "right",
            "type": "default",
        },
        {
            "id": "reactflow__edge-tool-4right-llm-2right",
            "source": "tool-4",
            "target": "llm-2",
            "sourceHandle": "right",
            "targetHandle": "right",
            "type": "default",
        },
    ],
    "metadata": {
        "entry_point": "llm-2",
        "start_connections": [{"target": "llm-2", "type": "default"}],
        "end_connections": [{"source": "llm-2", "type": "smoothstep"}],
    },
}
config_n_new={
  "id": "b18a9cb2-85b1-4344-bede-8d532193cbee",
  "name": "Flow Visualization",
  "nodes": [
    {
      "id": "start-1",
      "type": "start",
      "position": {
        "x": 77,
        "y": 222
      },
      "data": {
        "label": "Start"
      }
    },
    {
      "id": "llm-2",
      "type": "llm",
      "position": {
        "x": 409,
        "y": 195
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "llm-3",
      "type": "llm",
      "position": {
        "x": 810,
        "y": 87
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "llm-4",
      "type": "llm",
      "position": {
        "x": 792,
        "y": 431
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "tool-5",
      "type": "tool",
      "position": {
        "x": 1161,
        "y": 275
      },
      "data": {
        "label": "Tool",
        "tools": [
          "calculator"
        ]
      }
    },
    {
      "id": "tool-6",
      "type": "tool",
      "position": {
        "x": 1151.59970703125,
        "y": 548.2
      },
      "data": {
        "label": "Tool",
        "tools": [
          "calculator"
        ]
      }
    },
    {
      "id": "llm-7",
      "type": "llm",
      "position": {
        "x": 699.59970703125,
        "y": 712.2
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    }
  ],
  "edges": [
    {
      "id": "reactflow__edge-start-1right-llm-2left",
      "source": "start-1",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-2right-llm-3left",
      "source": "llm-2",
      "target": "llm-3",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-2right-llm-4left",
      "source": "llm-2",
      "target": "llm-4",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-3right-tool-5left",
      "source": "llm-3",
      "target": "tool-5",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-tool-5right-llm-3right",
      "source": "tool-5",
      "target": "llm-3",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-4right-tool-6left",
      "source": "llm-4",
      "target": "tool-6",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-tool-6right-llm-4right",
      "source": "tool-6",
      "target": "llm-4",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-4right-llm-2right",
      "source": "llm-4",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-3right-llm-2right",
      "source": "llm-3",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-2right-llm-7left",
      "source": "llm-2",
      "target": "llm-7",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-7right-llm-2right",
      "source": "llm-7",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    }
  ],
  "metadata": {
    "entry_point": "llm-2",
    "start_connections": [
      {
        "target": "llm-2",
        "type": "default"
      }
    ],
    "end_connections": []
  }
}

config_with_tools = {
    "id": "b136b7fe-3ddb-4ced-8b64-cc8065c566a2",
    "name": "Flow Visualization",
    "nodes": [
        {
            "id": "llm-1",
            "type": "llm",
            "position": {"x": 361, "y": 178},
            "data": {
                "label": "LLM",
                "model": "glm-4",
                "temperature": 0.7,
            },
        },
        {
            "id": "tool-2",
            "type": "tool",
            "position": {"x": 558, "y": 368},
            "data": {
                "label": "Tool",
                "tools": ["calculator", "tavilysearch"],
            },
        },
        {
            "id": "start-3",
            "type": "start",
            "position": {"x": 117, "y": 233},
            "data": {"label": "Start"},
        },
        {
            "id": "end-4",
            "type": "end",
            "position": {"x": 775, "y": 133},
            "data": {"label": "End"},
        },
    ],
    "edges": [
        {
            "id": "reactflow__edge-start-3right-llm-1left",
            "source": "start-3",
            "target": "llm-1",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "default",
        },
        {
            "id": "reactflow__edge-llm-1right-tool-2left",
            "source": "llm-1",
            "target": "tool-2",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "smoothstep",
        },
        {
            "id": "reactflow__edge-llm-1right-end-4left",
            "source": "llm-1",
            "target": "end-4",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "smoothstep",
        },
        {
            "id": "reactflow__edge-tool-2right-llm-1right",
            "source": "tool-2",
            "target": "llm-1",
            "sourceHandle": "right",
            "targetHandle": "right",
            "type": "default",
        },
    ],
    "metadata": {
        "entry_point": "llm-1",
        "start_connections": [{"target": "llm-1", "type": "default"}],
        "end_connections": [{"source": "llm-1", "type": "smoothstep"}],
    },
}

config_with_no_tools = {
    "id": "4613d429-88bb-4fe5-9b45-b5a5d3795dbf",
    "name": "Flow Visualization",
    "nodes": [
        {
            "id": "start-1",
            "type": "start",
            "position": {"x": 103, "y": 138},
            "data": {"label": "Start"},
        },
        {
            "id": "llm-2",
            "type": "llm",
            "position": {"x": 562, "y": 166},
            "data": {"label": "LLM", "model": "glm-4", "temperature": 0.7},
        },
        {
            "id": "end-3",
            "type": "end",
            "position": {"x": 1058, "y": 224},
            "data": {"label": "End"},
        },
    ],
    "edges": [
        {
            "id": "reactflow__edge-start-1right-llm-2left",
            "source": "start-1",
            "target": "llm-2",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "default",
        },
        {
            "id": "reactflow__edge-llm-2right-end-3left",
            "source": "llm-2",
            "target": "end-3",
            "sourceHandle": "right",
            "targetHandle": "left",
            "type": "default",
        },
    ],
    "metadata": {
        "entry_point": "llm-2",
        "start_connections": [{"target": "llm-2", "type": "default"}],
        "end_connections": [{"source": "llm-2", "type": "default"}],
    },
}

config_with_3_llm ={
  "id": "afc2672d-4981-417c-9857-dc2c882e824e",
  "name": "Flow Visualization",
  "nodes": [
    {
      "id": "start-1",
      "type": "start",
      "position": {
        "x": 108,
        "y": 199
      },
      "data": {
        "label": "Start"
      }
    },
    {
      "id": "llm-2",
      "type": "llm",
      "position": {
        "x": 485,
        "y": 230
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "llm-3",
      "type": "llm",
      "position": {
        "x": 903,
        "y": 287
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "llm-4",
      "type": "llm",
      "position": {
        "x": 1249.0744537815124,
        "y": 403.6915966386555
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "end-5",
      "type": "end",
      "position": {
        "x": 1622.224033613445,
        "y": 439.4517647058824
      },
      "data": {
        "label": "End"
      }
    }
  ],
  "edges": [
    {
      "id": "reactflow__edge-start-1right-llm-2left",
      "source": "start-1",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-2right-llm-3left",
      "source": "llm-2",
      "target": "llm-3",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-3right-llm-4left",
      "source": "llm-3",
      "target": "llm-4",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-4right-end-5left",
      "source": "llm-4",
      "target": "end-5",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "default"
    }
  ],
  "metadata": {
    "entry_point": "llm-2",
    "start_connections": [
      {
        "target": "llm-2",
        "type": "default"
      }
    ],
    "end_connections": [
      {
        "source": "llm-4",
        "type": "default"
      }
    ]
  }
}

config_hierarchical = {
  "id": "5523ef3c-bc48-4c05-8ec3-9a06792a31dd",
  "name": "Flow Visualization",
  "nodes": [
    {
      "id": "start-1",
      "type": "start",
      "position": {
        "x": -44.15113636363634,
        "y": 323.94204545454545
      },
      "data": {
        "label": "Start"
      }
    },
    {
      "id": "llm-2",
      "type": "llm",
      "position": {
        "x": 298.6136363636364,
        "y": 294.8636363636364
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "llm-3",
      "type": "llm",
      "position": {
        "x": 977.4636363636364,
        "y": 190.3522727272727
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "tool-4",
      "type": "tool",
      "position": {
        "x": 1203.7329545454545,
        "y": 67.97386363636363
      },
      "data": {
        "label": "Tool",
        "tools": [
          "calculator"
        ]
      }
    },
    {
      "id": "llm-6",
      "type": "llm",
      "position": {
        "x": 585.881915838068,
        "y": 592.4579545454545
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "llm-7",
      "type": "llm",
      "position": {
        "x": 1058.00009765625,
        "y": 776
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "end-7",
      "type": "end",
      "position": {
        "x": 607.6921431107955,
        "y": -8.914090909090909
      },
      "data": {
        "label": "End"
      }
    }
  ],
  "edges": [
    {
      "id": "reactflow__edge-start-1right-llm-2left",
      "source": "start-1",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-2right-llm-3left",
      "source": "llm-2",
      "target": "llm-3",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-3right-tool-4left",
      "source": "llm-3",
      "target": "tool-4",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-tool-4right-llm-3right",
      "source": "tool-4",
      "target": "llm-3",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-2right-llm-6left",
      "source": "llm-2",
      "target": "llm-6",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-6right-llm-7left",
      "source": "llm-6",
      "target": "llm-7",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-7right-llm-6right",
      "source": "llm-7",
      "target": "llm-6",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-6right-llm-2right",
      "source": "llm-6",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-2right-end-7left",
      "source": "llm-2",
      "target": "end-7",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-3right-llm-2right",
      "source": "llm-3",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    }
  ],
  "metadata": {
    "entry_point": "llm-2",
    "start_connections": [
      {
        "target": "llm-2",
        "type": "default"
      }
    ],
    "end_connections": [
      {
        "source": "llm-2",
        "type": "smoothstep"
      }
    ]
  }
}
config_sequential_with_tools={
  "id": "d4962554-d4ea-4a02-9067-eabf4d2e505b",
  "name": "Flow Visualization",
  "nodes": [
    {
      "id": "start-1",
      "type": "start",
      "position": {
        "x": 84,
        "y": 191
      },
      "data": {
        "label": "Start"
      }
    },
    {
      "id": "llm-2",
      "type": "llm",
      "position": {
        "x": 487,
        "y": 217
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "llm-3",
      "type": "llm",
      "position": {
        "x": 913,
        "y": 238
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "llm-4",
      "type": "llm",
      "position": {
        "x": 1269,
        "y": 235
      },
      "data": {
        "label": "LLM",
        "model": "glm-4",
        "temperature": 0.7
      }
    },
    {
      "id": "tool-5",
      "type": "tool",
      "position": {
        "x": 707,
        "y": 520
      },
      "data": {
        "label": "Tool",
        "tools": [
          "calculator"
        ]
      }
    },
    {
      "id": "tool-6",
      "type": "tool",
      "position": {
        "x": 1122,
        "y": 589
      },
      "data": {
        "label": "Tool",
        "tools": [
          "calculator"
        ]
      }
    },
    {
      "id": "tool-7",
      "type": "tool",
      "position": {
        "x": 1568,
        "y": 569
      },
      "data": {
        "label": "Tool",
        "tools": [
          "calculator"
        ]
      }
    },
    {
      "id": "end-8",
      "type": "end",
      "position": {
        "x": 1763,
        "y": 257
      },
      "data": {
        "label": "End"
      }
    }
  ],
  "edges": [
    {
      "id": "reactflow__edge-start-1right-llm-2left",
      "source": "start-1",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-2right-llm-3left",
      "source": "llm-2",
      "target": "llm-3",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-3right-llm-4left",
      "source": "llm-3",
      "target": "llm-4",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-llm-2right-tool-5left",
      "source": "llm-2",
      "target": "tool-5",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-tool-5right-llm-2right",
      "source": "tool-5",
      "target": "llm-2",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-3right-tool-6left",
      "source": "llm-3",
      "target": "tool-6",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-tool-6right-llm-3right",
      "source": "tool-6",
      "target": "llm-3",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-4right-tool-7left",
      "source": "llm-4",
      "target": "tool-7",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    },
    {
      "id": "reactflow__edge-tool-7right-llm-4right",
      "source": "tool-7",
      "target": "llm-4",
      "sourceHandle": "right",
      "targetHandle": "right",
      "type": "default"
    },
    {
      "id": "reactflow__edge-llm-4right-end-8left",
      "source": "llm-4",
      "target": "end-8",
      "sourceHandle": "right",
      "targetHandle": "left",
      "type": "smoothstep"
    }
  ],
  "metadata": {
    "entry_point": "llm-2",
    "start_connections": [
      {
        "target": "llm-2",
        "type": "default"
      }
    ],
    "end_connections": [
      {
        "source": "llm-4",
        "type": "smoothstep"
      }
    ]
  }
}