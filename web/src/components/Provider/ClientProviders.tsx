"use client";

import { useEffect } from "react";

import { OpenAPI } from "@/client";

const ClientProvider = ({ children }: { children: React.ReactNode }) => {
  useEffect(() => {
    OpenAPI.BASE = "http://127.0.0.1:5173";
    OpenAPI.TOKEN = async () => {
      return localStorage.getItem("access_token") || "";
    };
  }, []);

  return <>{children}</>;
};

export default ClientProvider;
