"use client";
import React, { useCallback, useMemo, KeyboardEvent, useState } from "react";
import ReactFlow, {
  Background,
  Controls,
  MiniMap,
  Node,
  Edge,
  ConnectionLineType,
  Connection,
  useReactFlow,
  MarkerType,
  Panel,
  useViewport,
} from "reactflow";
import "reactflow/dist/style.css";
import NodePalette from "./NodePalette";
import {
  Box,
  Button,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  CloseButton,
  Kbd,
  useColorModeValue,
  Text,
} from "@chakra-ui/react";
import { nodeConfig, NodeType } from "./nodes/nodeConfig";
import BaseProperties from "./nodes/Base/Properties";
import { CustomNode, FlowVisualizerProps } from "./types";
import { useFlowState } from "@/hooks/graphs/useFlowState";
import { useContextMenu } from "@/hooks/graphs/useContextMenu";
import { useGraphConfig } from "@/hooks/graphs/useUpdateGraphConfig";
import { MdBuild, MdOutlineHelp } from "react-icons/md";

const FlowVisualizer: React.FC<FlowVisualizerProps> = ({
  nodeTypes,
  defaultEdgeOptions,
  teamId,
  graphData,
}) => {
  const {
    nodes,
    setNodes,
    edges,
    setEdges,
    selectedNodeId,
    setSelectedNodeId,
    onNodesChange,
    onEdgesChange,
    onConnect,
    onNodeDataChange,
    nameError,
  } = useFlowState(
    graphData?.data[0]?.config?.nodes,
    graphData?.data[0]?.config?.edges
  );

  const { contextMenu, onNodeContextMenu, closeContextMenu } = useContextMenu();
  const buttonColor = useColorModeValue("ui.main", "ui.main");
  const reactFlowInstance = useReactFlow();

  const onNodeClick = useCallback(
    (event: React.MouseEvent, node: Node) => {
      setSelectedNodeId(node.id);
    },
    [setSelectedNodeId]
  );

  const nodesWithSelection = useMemo(() => {
    return nodes?.map((node) => ({
      ...node,
      style: {
        ...node.style,
        border: node.id === selectedNodeId ? "2px solid #2970ff" : "none",
        borderRadius: "8px",
      },
    }));
  }, [nodes, selectedNodeId]);

  const getNodePropertiesComponent = (node: Node | null) => {
    if (!node) return null;

    const nodeType = node.type as NodeType;
    const PropertiesComponent = nodeConfig[nodeType]?.properties;

    return (
      <BaseProperties
        nodeName={node.data.label}
        onNameChange={(newName: string) =>
          onNodeDataChange(node.id, "label", newName)
        }
        nameError={nameError}
      >
        {PropertiesComponent && (
          <PropertiesComponent
            node={node}
            onNodeDataChange={onNodeDataChange}
          />
        )}
      </BaseProperties>
    );
  };

  const isValidConnection = useCallback(
    (connection: Connection) => {
      const sourceNode = nodes.find((node) => node.id === connection.source);
      const targetNode = nodes.find((node) => node.id === connection.target);

      if (!sourceNode || !targetNode) return false;

      const sourceType = sourceNode.type as NodeType;
      const targetType = targetNode.type as NodeType;

      const sourceAllowedConnections =
        nodeConfig[sourceType].allowedConnections;
      const targetAllowedConnections =
        nodeConfig[targetType].allowedConnections;

      // 检查源节点是否允许从指定的 handle 连出
      if (
        connection.sourceHandle &&
        !sourceAllowedConnections.sources.includes(connection.sourceHandle)
      ) {
        return false;
      }
      // 检查目标节点是否允许从指定的 handle 连入
      if (
        connection.targetHandle &&
        !targetAllowedConnections.targets.includes(connection.targetHandle)
      ) {
        return false;
      }
      // 防止自连接
      if (connection.source === connection.target) return false;
      // 防止重复连接
      const existingEdge = edges.find(
        (edge) =>
          edge.source === connection.source && edge.target === connection.target
      );
      if (existingEdge) return false;
      // 允许所有其他连接
      return true;
    },
    [nodes, edges]
  );

  const toggleEdgeType = useCallback(
    (edge: Edge) => {
      setEdges((eds) =>
        eds.map((e) => {
          if (e.id === edge.id) {
            const newType = e.type === "default" ? "smoothstep" : "default";
            return {
              ...e,
              type: newType,
              animated: newType !== "default",
              style: {
                strokeDasharray: newType === "default" ? "none" : "5,5",
              },
            };
          }
          return e;
        })
      );
    },
    [setEdges]
  );

  const onEdgeContextMenu = useCallback(
    (event: React.MouseEvent, edge: Edge) => {
      event.preventDefault();
      toggleEdgeType(edge);
    },
    [toggleEdgeType]
  );

  const onKeyDown = useCallback(
    (event: KeyboardEvent) => {
      if (event.key === "e" || event.key === "E") {
        const selectedEdges = edges.filter((e) => e.selected);
        selectedEdges.forEach(toggleEdgeType);
      }
    },
    [edges, toggleEdgeType]
  );

  const onDragOver = useCallback((event: React.DragEvent) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = "move";
  }, []);

  const generateUniqueName = useCallback(
    (baseLabel: string) => {
      const existingNames = nodes.map((node) => node.data.label);
      let counter = 1;
      let newName = baseLabel;
      while (existingNames.includes(newName)) {
        counter++;
        newName = `${baseLabel}${counter}`;
      }
      return newName;
    },
    [nodes]
  );

  const onDrop = useCallback(
    (event: React.DragEvent) => {
      event.preventDefault();
      const type = event.dataTransfer.getData(
        "application/reactflow"
      ) as NodeType;
      if (typeof type === "undefined" || !type) return;

      const position = reactFlowInstance.screenToFlowPosition({
        x: event.clientX,
        y: event.clientY,
      });
      const baseLabel = `${nodeConfig[type].display}`;
      const uniqueName = generateUniqueName(baseLabel);
      const newNode: CustomNode = {
        id: `${type}-${nodes.length + 1}`,
        type,
        position,
        data: {
          label: uniqueName, // 使用生成的唯一名称
          customName: uniqueName,
          onChange: (key: string, value: any) =>
            onNodeDataChange(`${type}-${nodes.length + 1}`, key, value),
          ...nodeConfig[type].initialData,
        },
      };

      setNodes((nds) => nds.concat(newNode));
    },
    [nodes, reactFlowInstance, setNodes, onNodeDataChange, generateUniqueName]
  );
  const closePropertiesPanel = useCallback(() => {
    setSelectedNodeId(null);
  }, [setSelectedNodeId]);
  const deleteNode = useCallback(() => {
    if (contextMenu.nodeId) {
      setNodes((nds) => nds.filter((node) => node.id !== contextMenu.nodeId));
      setEdges((eds) =>
        eds.filter(
          (edge) =>
            edge.source !== contextMenu.nodeId &&
            edge.target !== contextMenu.nodeId
        )
      );
    }
    closeContextMenu();
    closePropertiesPanel();
  }, [
    contextMenu.nodeId,
    setNodes,
    setEdges,
    closeContextMenu,
    closePropertiesPanel,
  ]);

  const {
    id: graphId,
    name: graphName,
    description: graphDescription,
  } = graphData?.data[0] || {};

  const { onSave, isLoading: isSaving } = useGraphConfig(
    teamId,
    graphId,
    graphName,
    graphDescription,
    nodes,
    edges
  );

  const memoizedNodeTypes = useMemo(() => nodeTypes, [nodeTypes]);
  const memoizedDefaultEdgeOptions = useMemo(
    () => defaultEdgeOptions,
    [defaultEdgeOptions]
  );
  const { zoom } = useViewport();

  const ZoomDisplay = () => (
    <Panel position="bottom-right">{Math.round(zoom * 100)}%</Panel>
  );

  const [isShortcutPanelVisible, setShortcutPanelVisible] = useState(false); // Add this state

  const toggleShortcutPanel = () => {
    setShortcutPanelVisible((prev) => !prev);
  };

  const hideShortcutPanel = () => {
    setShortcutPanelVisible(false);
  };
  return (
    <Box
      display="flex"
      height="100%"
      onKeyDown={onKeyDown}
      tabIndex={0}
      bg={"#f0f2f7"}
    >
      <NodePalette />
      <Box flex={1} position="relative">
        <ReactFlow
          onNodeClick={onNodeClick}
          nodes={nodesWithSelection}
          edges={edges?.map((edge) => ({
            ...edge,
            style: {
              ...edge.style,
              strokeDasharray: edge.type === "default" ? "none" : "5,5",
            },
          }))}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          isValidConnection={isValidConnection}
          onEdgeContextMenu={onEdgeContextMenu}
          onNodeContextMenu={onNodeContextMenu}
          nodeTypes={memoizedNodeTypes}
          defaultEdgeOptions={{
            ...memoizedDefaultEdgeOptions,
            markerEnd: {
              type: MarkerType.ArrowClosed,
              width: 20,
              height: 20,
              color: "#2970ff",
            },
            style: { strokeWidth: 2 },
          }}
          connectionLineType={ConnectionLineType.SmoothStep}
          onDragOver={onDragOver}
          onDrop={onDrop}
          deleteKeyCode={["Backspace", "Delete"]}
        >
          <Controls />

          <Background
            color="#f2f2f2"
            gap={16}
            style={{ background: "#f1f1f1" }}
          />
          <MiniMap />

          <Panel position="top-left">
            <MdOutlineHelp
              onMouseEnter={toggleShortcutPanel}
              onMouseLeave={hideShortcutPanel}
              cursor="pointer"
            />
            {isShortcutPanelVisible && (
              <Box bg="white" p={2} borderRadius="md" boxShadow="md">
                Shortcut:
                <br /> Change edges type:<Kbd>E</Kbd>
                <br />
                Delete:<Kbd>Backspace</Kbd> <Kbd>Delete</Kbd>
                <br />
                Info:
                <br /> solid line: Normal edge
                <br />
                dashed line: Conditional edge
              </Box>
            )}
          </Panel>
          <ZoomDisplay />
        </ReactFlow>
        {contextMenu.nodeId && (
          <Menu isOpen={true} onClose={closeContextMenu}>
            <MenuButton as={Button} style={{ display: "none" }} />
            <MenuList
              style={{
                position: "absolute",
                left: `${contextMenu.x}px`,
                top: `${contextMenu.y}px`,
              }}
            >
              <MenuItem onClick={deleteNode}>Delete Node</MenuItem>
            </MenuList>
          </Menu>
        )}
      </Box>
      {/* <Panel position="top-right" > */}
      <Button
        bg={buttonColor}
        borderRadius={"md"}
        onClick={onSave}
        isLoading={isSaving}
        loadingText="Saving..."
        _hover={{ backgroundColor: "#1c86ee" }}
        rightIcon={<MdBuild color={"white"} />}
        position={"absolute"}
        right={"20px"}
        top={"8px"}
      >
        <Text color={"white"}>Deploy</Text>
      </Button>
      {/* </Panel> */}
      {selectedNodeId && (
        <Box
          position="relative"
          width="250px"
          borderLeft="1px solid #ccc"
          p={4}
        >
          <CloseButton
            onClick={closePropertiesPanel}
            position="absolute"
            right={2}
            top={2}
            size={"lg"}
          />

          {getNodePropertiesComponent(
            nodes.find((n) => n.id === selectedNodeId) || null
          )}
        </Box>
      )}
    </Box>
  );
};

export default FlowVisualizer;