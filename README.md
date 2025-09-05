### Categories 
**Available Categories:**
- `erq-discovery` - Host and service discovery
- `erq-vuln` - Vulnerability identification  
- `erq-exploit` - Exploitation attempts
- `erq-auth` - Authentication testing
- `erq-all` - Run all scripts (⚠️ **Warning**: Lengthy execution time, generates multiple files, may have unexpected interactions)

*Note: The "erq" prefix prevents conflicts with existing Nmap categories.*# nmap-pentest-scripts
Custom Nmap NSE scripts designed to streamline penetration testing workflows with intelligent reporting.

## Main Idea
- **Four-phase attack methodology**: Scripts organized around Discovery, Vulnerabilities, Exploitation, and Authentication
- **Custom categories**: Run targeted script collections without hunting through individual files
- **Balanced complexity**: Simple enough for beginners to understand, sophisticated enough to be genuinely useful
- **Intelligent reporting**: Auto-extract and analyze key findings into separate report files
- **Flexible expertise levels**: Granular control allowing users to operate at their comfort level

## How to Use
I designed these scripts to be as straightforward as possible. While you can call individual scripts, I've created categories for each phase so you can run entire collections without tracking down each script manually. These categories are separate from Nmap's default categories (though those are preserved for advanced users).

### Categories 
To scan hosts, use this format:

```bash
nmap --script <CATEGORY> <target>
```

**Available Categories:**
- `erq-discovery` - Host and service discovery
- `erq-vuln` - Vulnerability identification  
- `erq-exploit` - Exploitation attempts
- `erq-auth` - Authentication testing
- `erq-all` - Run all scripts (⚠️ **Warning**: Lengthy execution time, generates multiple files, may have unexpected interactions)

*Note: The "erq" prefix prevents conflicts with existing Nmap categories.*

### Reports
What sets this apart from standard Nmap scanning is the intelligent reporting system. Rather than simply duplicating Nmap's output, these scripts:

- **Parse and prioritize** the most critical findings
- **Provide actionable insights** with integrity ratings
- **Suggest next steps** based on discovered information
- **Tailor recommendations** to the specific category:
  - **Discovery**: Highlights promising services for deeper investigation
  - **Vulnerabilities**: Identifies security gaps and suggests exploitation tools
  - **Exploitation**: Documents successful attacks and potential C2 channels
  - **Authentication**: Maps credential weaknesses and bypass opportunities

Every script execution automatically generates a focused report designed to guide your next moves.

## Project Philosophy
I built this because I love cybersecurity from a programming perspective. While I'm not the strongest under pressure during live penetration tests, I excel at methodical planning and tool development. My goal is to support security teams by creating flexible, helpful automation that enhances their capabilities.

I hope security professionals will use these scripts, provide feedback on their strengths and weaknesses, and help me iterate toward increasingly useful tools. Thank you for taking the time to explore this project—I hope it proves valuable in your security work!

## Development Status
This project is currently in active development. Here's the current progress:

### ✅ Completed
- [x] Project planning and architecture design
- [x] README documentation and project structure
- [x] Category naming convention (`erq-` prefix)

### 🚧 In Progress
- [ ] Discovery phase scripts (`erq-discovery`)
  - [ ] Host discovery scripts
  - [ ] Service enumeration scripts
  - [ ] Port scanning automation
- [ ] Vulnerability assessment scripts (`erq-vuln`)
  - [ ] Common vulnerability checks
  - [ ] Service-specific vulnerability scripts
  - [ ] CVE-based scanning scripts

### 📋 Planned
- [x] Exploitation scripts (`erq-exploit`)
  - [x] Basic exploitation script template (`ExploitBasics.nse`)
  - [ ] Common exploit attempts
  - [ ] Service-specific exploits
  - [ ] Payload delivery scripts
- [x] Authentication testing scripts (`erq-auth`)
  - [x] Basic authentication script template (`AuthBasics.nse`)
  - [ ] Brute force automation
  - [ ] Default credential checks
  - [ ] Authentication bypass tests
- [ ] Intelligent reporting system
  - [ ] Report parsing engine
  - [ ] Integrity rating system
  - [ ] Next-step recommendations
- [ ] Documentation and examples
  - [ ] Individual script documentation
  - [ ] Usage examples and tutorials
  - [ ] Best practices guide

### 🎯 Future Enhancements
- [ ] Integration with other security tools
- [ ] Custom output formats (JSON, XML, etc.)
- [ ] Automated report generation improvements
- [ ] Performance optimizations

*Last updated: September 2025*

## Contributing
Feedback, bug reports, and suggestions are always welcome. This project grows stronger through community input and real-world testing. Since this is an active development project, early feedback on the approach and planned features is especially valuable!