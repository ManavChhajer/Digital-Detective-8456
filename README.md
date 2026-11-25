# Digital Detective

> Diwali Independent Learning Assignment: an investigation of how computers really work.

- **Name:** Manav Chhajer
- **GitHub repository:** `https://github.com/ManavChhajer/Digital-Detective-8456`

---

## Missions

| # | Mission | Report | Evidence |
| :-: | :--- | :--- | :--- |
| 00 | Workspace setup | [README](./mission-00-setup/README.md) | `Mission-00-01` to `Mission-00-04` |
| 01 | Computer basics (IPOS) | [README](./mission-01-computer-basics/README.md) | `Mission-01-01` to `Mission-01-03` |
| 02 | Terminal and files | [README](./mission-02-terminal/README.md) | `Mission-02-01` to `Mission-02-03` |
| 03 | Operating system | [README](./mission-03-operating-system/README.md) | `Mission-03-01` to `Mission-03-03` |
| 04 | How programs run | [README](./mission-04-programs/README.md) | `Mission-04-01` |
| 05 | Numbers and data | [README](./mission-05-numbers-data/README.md) | `Mission-05-01` |
| 06 | Git and GitHub | [README](./mission-06-git-github/README.md) | `Mission-06-01`, `Mission-06-02` |
| 07 | Networking | [README](./mission-07-networking/README.md) | `Mission-07-01`, `Mission-07-02` |
| 08 | Final report | [README](./mission-08-final-report/README.md) | n/a |

Evidence files are named `Mission-NN-PP`: `NN` is the mission number and `PP` is the picture number.

## Topics I explored

| Area | What I covered |
| :--- | :--- |
| Computer basics | The IPOS cycle, CPU and RAM versus SSD, hardware versus software, and small computers inside everyday machines |
| Operating system | What the kernel does, processes and PIDs, absolute and relative paths, and read/write/execute permissions |
| Terminal | Moving around, `>` versus `>>`, copying and moving, flags such as `ls -lah`, pipes, and Homebrew |
| How programs run | Compilers versus interpreters, and how Python compiles to bytecode before its virtual machine runs it |
| Numbers and data | Binary, decimal and hex conversions, ASCII and UTF-8 |
| Git and GitHub | Staging versus committing, branches, commits, and a pull request merged with a merge commit |
| Networking | LAN, MAN and WAN, routers, DNS, packet switching, and what happens when a website loads |

## Running my code

Both scripts need Python 3 (I used 3.12.10). Open a terminal in the project folder first.

**Hello program**
```bash
python3 mission-04-programs/hello.py
```
```text
Hello, Detective! Case file opened.
```

**Number converter** (whole numbers only)
```bash
cd mission-05-numbers-data
python3 number_converter.py
```
Example run:
```text
Enter a whole number (0 or more): 99
Decimal 99 -> Binary 1100011 -> Hex 0x63
```
Typing something that isn't a number prints `Please enter digits only.`

## What I learned

1. **Every task is the same loop.** Typing a letter or opening a web page both go Input, Processing, Output, Storage. Only the parts involved change.
2. **The OS shares the machine.** It decides which process gets the CPU, keeps programs out of each other's memory, and checks permissions, so many programs can run at once safely.
3. **Translation can happen early or late.** Compiled programs are translated before they run and usually run faster. Interpreted ones are easier to change and test. Python does a bit of both.
4. **Everything is bits.** Hex is a short way to write binary, and UTF-8 lets one system store text from many languages.
5. **Git keeps work safe.** Small commits with clear messages, branches for changes, and a pull request to review them before they reach `main`.
6. **A web page takes many steps.** DNS finds the address, TCP connects, TLS encrypts, and HTTP asks for the page.

## Privacy

- My username and computer name are replaced with `<me>` in the reports and blurred in screenshots.
- Screenshots in `evidence/` were checked before upload. Where a username, owner column, home folder path or similar showed, I blurred it.
- Network results use public servers only (for example Google and `example.com`), and no home network details are shown.

## Submission

- **GitHub repository:** https://github.com/ManavChhajer/Digital-Detective-8456
- **Author:** Manav Chhajer 
- **Pull request:** https://github.com/ManavChhajer/Digital-Detective-8456/pull/1
- **Final report:** [Mission 8](./mission-08-final-report/README.md), including the full commit list
