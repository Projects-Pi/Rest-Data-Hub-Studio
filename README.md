## REST DataHub Studio Control (`rdsctl`) Documentation

### Table of Contents
1. Introduction
2. Prerequisites
3. Installation
4. Command Line Usage
    - 4.1. `up` - Start Docker Compose Services
    - 4.2. `build` - Build Docker Compose Services
    - 4.3. `down` - Stop Docker Compose Services
    - 4.4. `logs` - View Docker Compose Logs
5. Examples
    - 5.1. Starting Services
    - 5.2. Building Services
    - 5.3. Stopping Services
    - 5.4. Viewing Logs
6. Troubleshooting
7. Frequently Asked Questions (FAQ)
8. Contact Information
9. License

### 1. Introduction
The `rdsctl` tool is a command-line utility for managing Docker Compose services within different flows of the REST DataHub Studio project.

### 2. Prerequisites
Before using `rdsctl`, ensure you have the following prerequisites:
- Docker Compose installed
- Python 3.x
- Pip package manager

### 3. Installation
To install `rdsctl`, run:
```bash
pip install rdsctl
```

### 4. Command Line Usage
The `rdsctl` tool provides the following commands:

#### 4.1. `up` - Start Docker Compose Services
Start Docker Compose services for a specified flow.

Usage:
```bash
rdsctl up FLOW [--all] [--services SERVICES]
```

- `FLOW`: The name of the flow (e.g., AuthFlow).
- `--all`: Start all services for the flow.
- `--services SERVICES`: Specify specific services to start (comma-separated).

Example:
```bash
rdsctl up AuthFlow --all
```

#### 4.2. `build` - Build Docker Compose Services
Build Docker Compose services for a specified flow.

Usage:
```bash
rdsctl build FLOW [--services SERVICES]
```

- `FLOW`: The name of the flow (e.g., AuthFlow).
- `--services SERVICES`: Specify specific services to build (comma-separated).

Example:
```bash
rdsctl build AuthFlow
```

#### 4.3. `down` - Stop Docker Compose Services
Stop Docker Compose services for a specified flow.

Usage:
```bash
rdsctl down FLOW [--all] [--services SERVICES]
```

- `FLOW`: The name of the flow (e.g., AuthFlow).
- `--all`: Stop all services for the flow.
- `--services SERVICES`: Specify specific services to stop (comma-separated).

Example:
```bash
rdsctl down AuthFlow --all
```

#### 4.4. `logs` - View Docker Compose Logs
View Docker Compose logs for a specified flow or service.

Usage:
```bash
rdsctl logs FLOW [--service SERVICE]
```

- `FLOW`: The name of the flow (e.g., AuthFlow).
- `--service SERVICE`: Specify a service to view logs.

Example:
```bash
rdsctl logs AuthFlow
```

### 5. Examples
Here are some usage examples for different scenarios:

#### 5.1. Starting Services
- Start all services for a flow:
  ```bash
  rdsctl up AuthFlow --all
  ```
- Start specific services for a flow:
  ```bash
  rdsctl up AuthFlow --services Service1,Service2
  ```

#### 5.2. Building Services
- Build all services for a flow:
  ```bash
  rdsctl build AuthFlow
  ```
- Build specific services for a flow:
  ```bash
  rdsctl build AuthFlow --services Service1,Service2
  ```

#### 5.3. Stopping Services
- Stop all services for a flow:
  ```bash
  rdsctl down AuthFlow --all
  ```
- Stop specific services for a flow:
  ```bash
  rdsctl down AuthFlow --services Service1,Service2
  ```

#### 5.4. Viewing Logs
- View logs for all services in a flow:
  ```bash
  rdsctl logs AuthFlow
  ```
- View logs for a specific service in a flow:
  ```bash
  rdsctl logs AuthFlow --service Service1
  ```

### 6. Troubleshooting
If you encounter any issues while using `rdsctl`, please refer to the troubleshooting section for solutions to common problems.



