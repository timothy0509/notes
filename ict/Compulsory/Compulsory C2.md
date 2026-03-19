# Compulsory C2
# Web Authoring and Network Security

## 1. Basics of Web Pages
### Basic Components
*   **HTML**: Uses markups to describe the structure of the web page.
*   **CSS**: Describes the appearance of HTML elements.
*   **JavaScript**: Adds dynamic programs to HTML elements.

### Hypertext Markup Language (HTML)
HTML is not a programming language but a cross-platform language used to define elements in a web page.
*   **Workflow**:
    1.  **Client** sends `HTTP request` (method: GET, path: /index.html).
    2.  **Web server** sends `HTTP response` (status: 200, content-type: text/html).

### Basic HTML Markup
*   `<html>`: Root element of the HTML file.
*   `<head>`: Contains information about the file (e.g., `<title>`, `<script>`).
*   `<body>`: Contains visible content (headings, paragraphs, tables, images, hyperlinks, etc.).

#### Common Tags & Usage
*   **Headings**: `<h1>The largest title</h1>`, `<h2>Title 2</h2>`
*   **Paragraphs**: `<p>Paragraph 1</p>`
*   **Line break**: `<br>`
*   **Horizontal rule**: `<hr>`
*   **Comments**: `<!-- This is a comment -->` (will not be displayed)
*   **Pre-formatted text**: `<pre>...</pre>` (preserves spacing/formatting)

### Text Formatting Tags
| Tag | Usage | Example Result |
| :--- | :--- | :--- |
| `<b>` | Bold | **bold** |
| `<i>` | Italic | *italic* |
| `<u>` | Underline | <u>underline</u> |
| `<sup>` | Superscript | <sup>superscript</sup> |
| `<sub>` | Subscript | <sub>subscript</sub> |

### Attributes
*   **Font**: `<p style="font-family:Comic Sans MS">New font</p>`
*   **Size**: `<p style="font-size:10px">10 pixels font</p>`
*   **Alignment**: `<p style="text-align:right">Go to Right</p>`
*   **Color**: `<h1 style="color:red">This is a red title</h1>`

### Lists
*   **Unordered List (`<ul>`)**:
    ```html
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
    ```
*   **Ordered List (`<ol>`)**:
    ```html
    <ol>
      <li>Item 1</li>
      <li>Item 2</li>
    </ol>
    ```

### Images
*   Format: `<img src="image.png" alt="description" height="150">`

### Tables
*   Basic structure:
    ```html
    <table border="1" style="border-spacing:30">
      <tr style="height:50;vertical-align:top">
        <th>Title 1</th>
        <td>row 1 cell 1</td>
      </tr>
    </table>
    ```

### Hyperlinks
*   Usage: `<p><a href="https://www.google.com">Go to Google</a></p>`
*   Purpose: Directs the web page to another web page, file location, or specific location on a page.

### Frames
*   Embed another HTML file:
    ```html
    <iframe src="A.html" width="500" height="500"></iframe>
    ```

### Website Navigation
*   **Navigation bar**: Helps visitors understand information arrangement quickly.
*   **Site map**: Acts like a shopping directory, listing sections of the website in detail.
*   **Cross-platform**: Website can operate on different platforms (desktop vs. mobile).

---

# Network Security and Privacy Threats
## Malware
Programs that damage computer functions, steal data, gain unauthorized access, or attack networks.
*   **Types**: Virus, Worm, Trojan program, Spyware, Adware, Ransomware.
*   **Spreading methods**: Dynamic web pages, client-side scripts, communication software/email, freeware/shareware, storage devices.
*   **Threats**:
    *   Unauthorized access.
    *   Locked, modified, or destroyed information.
    *   Ransom demands.
    *   Exhausted resources/paralysed system.
    *   Remote control of device.

## Specific Attacks
*   **Man-in-the-Middle (MITM)**: Attacker intercepts or tampers with communication between two parties.
*   **Denial-of-Service (DoS)**: Hackers make a target server unable to provide services to users.

## Security Measures
*   **Antivirus software**: Scans and isolates infected files. Compare files against "virus signatures" in a database.
*   **Firewalls**:
    *   **Software Firewall**: Protects a single device/network; easier to install; lower cost.
    *   **Hardware Firewall**: Physical device; more efficient and stable; higher cost.
*   **Access Control**:
    1.  **Authentication**: Verifying user identity.
    2.  **Authorisation**: Granting access to data.
    3.  **Accounting**: Monitoring user access records.
*   **Wireless Security**:
    *   **WPA**: Uses Temporal Key Integrity Protocol (TKIP) for constantly changing keys.
    *   **WPA2**: Advanced version of WPA.
    *   **Hide Wi-Fi name**: Turning off SSID broadcast.
    *   **MAC Address Filtering**: Only allows specific MAC addresses (whitelist) on the network.
*   **VPN (Virtual Private Network)**: Establishes a "tunnel" to encrypt data packets and protect against unauthorized access.

## Browser/Online Privacy
*   **Settings**: Disable pop-ups/redirects, enable automatic browser updates.
*   **Eavesdropping**: Unauthorized interception of private communications.
*   **Social Engineering**: Manipulating trust to trick victims into disclosing information. Includes: Baiting, Quid pro quo, Catfishing, Pretexting, Phishing.
*   **Protection methods**:
    *   Clear browsing history/cookies.
    *   Turn off autofill.
    *   Use private browsing.
    *   Use a proxy server.
*   **Password Security**:
    *   At least 8 chars, mix of digits, uppercase, lowercase, special characters.
    *   No personal info, no simple patterns like "123456", no common words.
    *   Change regularly (e.g., every 3 months), do not reuse last 3, do not share.

***

# Network Security Measures

## Concepts
*   **Encryption**: Transforming data into unreadable form with a key.
*   **Decryption**: Reverse process of encryption.

## Types of Encryption
1.  **Private key encryption (Symmetric)**: Uses the *same* key for both encryption and decryption.
2.  **Public key encryption (Asymmetric)**:
    *   **Encryption mode**: Sender uses Recipient's *Public Key* to encrypt. Only the Recipient can decrypt using their own *Private Key*. Used for online banking.
    *   **Authentication mode**: Sender uses their own *Private Key* to encrypt (sign). Any recipient can decrypt using the Sender's *Public Key*. Basis for digital signatures.

## Public Key Infrastructure (PKI)
*   **Purposes**: Privacy, Authentication, Integrity, Non-repudiation.
*   **Process**: Sender encrypts with recipient's public key AND signs with their own private key. Recipient verifies with sender's public key and decrypts with their own private key.

## Authentication Methods
*   Username and password
*   Token
*   Smart card
*   Biometrics
*   Digital certificate

## Multi-factor Authentication
*   **Something you KNOW**: Password, PIN, Security questions.
*   **Something you HAVE**: Token, Smart card, Mobile phone.
*   **Something you ARE**: Fingerprint, Facial scan, Voiceprint.

## Misconceptions
*   **Digital signature $\neq$ Electronic signature.**
*   **Dual password authentication $\neq$ 2FA.**
*   **HTTPS** does not secure data *in* the database; it secures data *during* the transmission process.
*   **Cookies**: Closing incognito browsers deletes cookies immediately.