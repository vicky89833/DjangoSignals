# Python & Django Tasks

This repository contains solutions for two distinct programming tasks:
1. **Django Signals Behavior Analysis**
2. **Custom Rectangle Class Implementation**

---

## Task 1: Django Signals Behavior Analysis

### Overview
This task investigates three key behaviors of Django signals:
1. Synchronous vs. asynchronous execution
2. Thread execution context
3. Database transaction behavior

### Implementation
- Created a Django project (`signal_test`) with a dedicated app (`signal_app`)
- Implemented signal handlers for `pre_save` and `post_save` signals
- Added thread and transaction analysis in signal handlers

### Key Findings
1. **Signals execute synchronously** (blocking)
2. **Signals run in the same thread** as the caller
3. **Signals respect database transactions**

### How to Test
1. Clone the repository
2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
