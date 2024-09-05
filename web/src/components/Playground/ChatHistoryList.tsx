import {
  Flex,
  Spinner,
  Container,
  useColorModeValue,
  IconButton,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Icon,
  Box,
  Text,
  Button,
} from "@chakra-ui/react";
import { useMutation, useQuery, useQueryClient } from "react-query";
import { MembersService, ThreadsService, type ApiError } from "../../client";
import useCustomToast from "../../hooks/useCustomToast";
import { useRouter } from "next/navigation";

import React, { useEffect, useState } from "react";
import { EllipsisVerticalIcon, StarIcon, Trash } from "lucide-react";
import useChatMessageStore from "@/store/chatMessageStore";

interface ChatHistoryProps {
  teamId: string;
}

const ChatHistoryList = ({ teamId }: ChatHistoryProps) => {
  const queryClient = useQueryClient();

  const navigate = useRouter();
  const showToast = useCustomToast();
  const rowTint = useColorModeValue("blackAlpha.50", "whiteAlpha.50");
  const [localTeamId, setLocalTeamId] = useState(teamId);
  useEffect(() => {
    setLocalTeamId(teamId);
  }, [teamId]);

  const {
    data: members,
    isLoading: membersLoading,
    isError: membersIsError,
    error: membersError,
  } = useQuery(
    ["teams", localTeamId, "members"],
    () => MembersService.readMembers({ teamId: Number.parseInt(localTeamId) }),
    {
      enabled: !!localTeamId, // 确保在 localTeamId 存在时才执行查询
    }
  );

  const {
    data: threads,
    isLoading,
    isError,
    error,
  } = useQuery(["threads", teamId], () =>
    ThreadsService.readThreads({ teamId: Number.parseInt(teamId) })
  );

  const deleteThread = async (threadId: string) => {
    await ThreadsService.deleteThread({
      teamId: Number.parseInt(teamId),
      id: threadId,
    });
  };
  const selctedColor = useColorModeValue(
    "ui.selctedColor",
    "ui.selctedColorDark"
  );
  const deleteThreadMutation = useMutation(deleteThread, {
    onError: (err: ApiError) => {
      const errDetail = err.body?.detail;
      showToast("Unable to delete thread.", `${errDetail}`, "error");
    },
    onSettled: () => {
      queryClient.invalidateQueries(["threads", teamId]);
      // queryClient.invalidateQueries(["thread", threadId]);
    },
  });
  const [selectedThreadId, setSelectedThreadId] = useState<string | null>(null);
  const onClickRowHandler = (threadId: string) => {
    navigate.push(`/playground?teamId=${teamId}&threadId=${threadId}`);
    setSelectedThreadId(threadId);
  };

  const { isOpen, onOpen, onClose } = useDisclosure();

  const onDeleteHandler = (threadId: string) => {
    setSelectedThreadId(threadId);
    onOpen();
  };
  const { setMessages } = useChatMessageStore();
  const handleDeleteConfirm = () => {
    if (selectedThreadId) {
      deleteThreadMutation.mutate(selectedThreadId);
      onClose();
      setMessages([]);
      navigate.push(`/playground?teamId=${teamId}`);
    }
  };

  if (isError) {
    const errDetail = (error as ApiError).body?.detail;

    showToast("Something went wrong.", `${errDetail}`, "error");
  }
  const [showMenu, setShowMenu] = useState(false);
  return (
    <>
      {isLoading ? (
        <Flex justify="center" align="center" height="100vh" width="full">
          <Spinner size="xl" color="ui.main" />
        </Flex>
      ) : (
        <Box h="full" maxH={"full"} overflow={"hidden"}>
          {threads && members && (
            <>
              <Box p={4} display="flex" overflow={"hidden"}>
                <Text fontSize="lg" fontWeight="bold">
                  聊天记录
                </Text>
              </Box>
              <Box overflowY={"auto"} overflowX={"hidden"} maxH="full" h="full">
                {threads.data.map((thread) => (
                  <Box
                    key={thread.id}
                    width={"full"}
                    borderRadius="md"
                    borderColor={rowTint}
                    cursor="pointer"
                    onClick={() => onClickRowHandler(thread.id)}
                    _hover={{ backgroundColor: rowTint }}
                    position="relative" // Ensure menu is positioned relative to this container
                    overflow={"hidden"}
                    onMouseEnter={() => {
                      setShowMenu(true);
                    }}
                    onMouseLeave={() => {
                      setShowMenu(false);
                    }}
                    backgroundColor={
                      selectedThreadId === thread.id.toString()
                        ? selctedColor
                        : "transparent"
                    }
                  >
                    <Box
                      display="flex"
                      alignItems="center"
                      alignContent="center"
                      flexDirection="row"
                      pt={4}
                      pb={4}
                      overflow={"hidden"}
                    >
                      <Icon as={StarIcon} mx={2} />
                      <Box mr={2} minW={"45%"} maxW={"45%"}>
                        <Text
                          fontFamily="Arial, sans-serif"
                          fontSize={"sm"}
                          color="gray.500"
                          noOfLines={1}
                        >
                          {thread.query}
                        </Text>
                      </Box>
                      <Box mr={2} minW={"55%"} maxW={"55%"}>
                        <Text
                          fontFamily="Arial, sans-serif"
                          fontSize={"sm"}
                          color={"gray.500"}
                          noOfLines={1}
                        >
                          {new Date(thread.updated_at).toLocaleString()}
                        </Text>
                      </Box>
                      {showMenu && (
                        <Box
                          display="flex"
                          position={"absolute"}
                          right={2}
                          ml={1}
                        >
                          <Menu>
                            <MenuButton
                              as={IconButton}
                              aria-label="Options"
                              icon={
                                <Icon as={EllipsisVerticalIcon} w="4" h="4" />
                              }
                              variant="ghost"
                            />
                            <MenuList>
                              <MenuItem
                                onClick={() => onDeleteHandler(thread.id)}
                              >
                                <Icon as={Trash} mr={2} />
                                <Text fontSize={"sm"}>删除</Text>
                              </MenuItem>
                            </MenuList>
                          </Menu>
                        </Box>
                      )}
                    </Box>
                  </Box>
                ))}
              </Box>
            </>
          )}
        </Box>
      )}
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Delete Thread</ModalHeader>
          <ModalCloseButton />
          <ModalBody>Are you sure you want to delete this thread?</ModalBody>
          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={handleDeleteConfirm}>
              Delete
            </Button>
            <Button onClick={onClose}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
};

export default ChatHistoryList;
