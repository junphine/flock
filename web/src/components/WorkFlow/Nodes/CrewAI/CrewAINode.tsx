import { Text, Tag } from "@chakra-ui/react";
import React from "react";
import { Handle, type NodeProps, Position } from "reactflow";

import { BaseNode } from "../Base/BaseNode";
import { nodeConfig } from "../nodeConfig";
import { CrewAINodeData } from "../../types";

const CrewAINode: React.FC<NodeProps> = (props) => {
  const { icon: Icon, colorScheme } = nodeConfig.crewai;
  const data = props.data as CrewAINodeData;

  return (
    <BaseNode {...props} icon={<Icon />} colorScheme={colorScheme}>
      <Handle type="target" position={Position.Left} id="left" />
      <Handle type="target" position={Position.Right} id="right" />
      <Handle type="source" position={Position.Left} id="left" />
      <Handle type="source" position={Position.Right} id="right" />

      <Tag
        size="sm"
        alignSelf="center"
        colorScheme={data.process_type === "sequential" ? "blue" : "purple"}
      >
        Agents Type: {data.process_type}
      </Tag>
    </BaseNode>
  );
};

export default React.memo(CrewAINode);