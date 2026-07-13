# 🛡️ CID Investigation REST API

A **Crime Investigation Department (CID) Management System** built with **Django** and **Django REST Framework (DRF)**. This project provides RESTful APIs to manage Officers, Criminals, Cases, Evidence, and Witnesses — with built-in search, filtering, ordering, and pagination.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![DRF](https://img.shields.io/badge/DRF-REST_Framework-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

This system digitizes core CID workflows — officer records, criminal databases, registered cases, collected evidence, and witness statements — and exposes them as clean, filterable REST APIs, along with a Django Admin panel for internal management.

---

## ✨ Features

- 👮 **Officer Management** — Track rank, joining date, and assigned cases
- 🕵️ **Criminal Database** — Store aliases, criminal history, wanted status
- 📁 **Case Registry** — Link officers & criminals to registered cases with status tracking
- 🔬 **Evidence Tracking** — Fingerprint, DNA, CCTV, Weapon, RDX residue, and more
- 🗣️ **Witness Records** — Statements linked to specific cases
- 🔎 **Search, Filter & Ordering** on every API endpoint
- 📄 **Pagination** (page size configurable via settings)
- 🖥️ **Django Admin Panel** with custom list displays & search fields
- 🎨 **Landing Page** built with Bootstrap 5 + Font Awesome showing live stats

---

## 🛠️ Tech Stack

| Layer          | Technology                          |
|----------------|--------------------------------------|
| Backend        | Python, Django                      |
| API            | Django REST Framework (DRF)         |
| Database       | SQLite (default, easily swappable)  |
| Frontend       | Bootstrap 5, Font Awesome, HTML/CSS |
| Admin Panel    | Django Admin                        |

---

## 📂 Project Structure
