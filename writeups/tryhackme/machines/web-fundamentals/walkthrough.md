---
layout: post
title: "TryHackMe Web Fundamentals - Level 1 Walkthrough"
date: 2024-10-28 14:30:00 +0000
categories: [tryhackme, web security, fundamentals]
tags: [web, http, html, burp suite]
---

# TryHackMe Web Fundamentals - Level 1 Walkthrough

**Room Link:** [https://tryhackme.com/rooms/web-fundamentals](https://tryhackme.com/rooms/web-fundamentals)
**Date Completed:** 2024-10-28
**Objective:** Understand HTTP requests and responses, inspect HTML source code, and use Burp Suite to intercept traffic.

## Overview

This room introduces the basics of web application interaction. We'll learn how browsers communicate with servers using HTTP, examine the structure of HTML pages, and utilize Burp Suite as a proxy to observe and modify network traffic.

## Task 1: Inspecting the Source Code

**Challenge:** View the source code of the provided webpage.

**My Approach:** I right-clicked on the page in my browser (Firefox) and selected "View Page Source." This revealed the underlying HTML structure, including hidden comments and JavaScript code.

**Screenshot:** [Screenshot showing Firefox's "View Page Source" window]

**Key Takeaway:** Understanding how a webpage is constructed using HTML is crucial for identifying potential vulnerabilities or hidden information.  Comments often contain valuable clues.

## Task 2: HTTP Requests & Responses

**Challenge:** Use Burp Suite to intercept and analyze an HTTP request and response.

**My Approach:** I configured my browser (Firefox) to use Burp Suite as a proxy (127.0.0.1:8080).  Then, I navigated to the target webpage. In Burp Suite's "Proxy" tab, I observed the HTTP request being sent from my browser to the server and the corresponding response received.

**Burp Suite Configuration:**
*   Proxy Listener: Enabled on 127.0.0.1:8080
*   Browser Proxy Settings: Set to use 127.0.0.1 port 8080

**Example HTTP Request (Snippet):**
```http
GET / HTTP/1.1
Host: web-fundamentals.thm
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Connection: keep-alive

**Example HTTP Response (Snippet):**

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Sun, 27 Oct 2024 14:30:00 GMT
Server: THM

<!DOCTYPE html>
<html>
... (rest of the HTML content) ...
</html>
