Write-up: Roasted Challenge Category: Cryptography  
Difficulty: Hard  
Key Concepts: Hidden Subset Sum Problem (HSSP), LLL Algorithm, Side-Channel Attack, Lattice Reduction Challenge Overview We are provided with a server that runs a "flag guessing" game. In Exponent Mode, for every guess we make, the server:

1. Generates a random 128-bit exponent $e$.
    
2. Updates a running total_score using a hidden modulus $N$.
    
3. Returns $e$ and the new total_score. The score update mechanism (inferred) is: $$ \text{score}_{new} = (\text{score}_{old} + (\text{base} \times \text{multiplier})^e) \pmod N $$ The multiplier depends on the quality of our guess:
    

- Incorrect guess: Multiplier is $-1$.
    
- Correct guess (substring of flag): Multiplier is $2$. Our goal is to recover the flag. However, we don't know $N$, so we cannot directly verify the score updates. Solution Strategy Phase 1: Recovering N (The "Hidden Subset Sum" Attack) Since $N$ is unknown, we cannot directly reverse the math. However, we can treat the exponents as a Hidden Subset Sum Problem. If we send a "garbage" guess (e.g., "IMPOSSIBLE"), we know the multiplier is $-1$. Let $\Delta_i$ be the difference in score for the $i$-th query: $$ \Delta_i \equiv (\text{base} \cdot -1)^{e_i} \pmod N $$ If we can find a set of integer coefficients $c_i$ such that a linear combination of the exponents sums to zero: $$ \sum_{i} c_i e_i = 0 $$ Then, applying these coefficients to the observed score differences yields a powerful relation: $$ \prod_{i} \Delta_i^{c_i} \equiv \prod_{i} (\text{base} \cdot -1)^{c_i e_i} \equiv (\text{base} \cdot -1)^{\sum c_i e_i} \equiv (\text{base} \cdot -1)^{0} \equiv 1 \pmod N $$ This means that $X = \left(\prod \Delta_i^{c_i}\right) - 1$ is a multiple of $N$. By finding a few such relations and computing the GCD of the resulting $X$ values, we can recover $N$. Lattice Construction: We use the LLL algorithm to find the coefficients $c_i$. We construct a lattice matrix where we look for small vectors orthogonal to the vector of exponents $E = [e_1, e_2, \dots, e_m]$. Basis Matrix (for $m=21$ samples): $$ M = \begin{pmatrix} 1 & 0 & \dots & 0 & K \cdot e_1 \ 0 & 1 & \dots & 0 & K \cdot e_2 \ \vdots & \vdots & \ddots & \vdots & \vdots \ 0 & 0 & \dots & 1 & K \cdot e_m \end{pmatrix} $$ Where $K$ is a large constant (e.g., $10^{40}$) to penalize the last column, ensuring the linear combination of exponents is strictly zero. Phase 2: Brute-Forcing the Flag Once $N$ is recovered, the challenge becomes a standard oracle attack. We know the flag starts with firebird{. We brute-force the flag character by character.
    

1. Let the current known prefix be $P$.
    
2. Try appending a character $x$ to form guess $P + x$.
    
3. Send the guess to the server. Receive $e_{new}$ and score difference $\Delta_{new}$.
    
4. Validation: We compare this new sample against a known "incorrect" reference sample $(e_{ref}, \Delta_{ref})$.
    
    If our guess is incorrect (multiplier -1): $$ \Delta_{new} \equiv (\text{base} \cdot -1)^{e_{new}} \pmod N $$
    
    This implies the following invariant must hold: $$ \Delta_{new}^{e_{ref}} \equiv ((\text{base} \cdot -1)^{e_{new}})^{e_{ref}} \equiv ((\text{base} \cdot -1)^{e_{ref}})^{e_{new}} \equiv \Delta_{ref}^{e_{new}} \pmod N $$
    
    If this equality fails, it implies our guess had a different multiplier (i.e., 2), meaning the character is correct. Implementation (Solver Script) Here is the complete solution script that recovers $N$ and extracts the flag. import socket import time from math import gcd import string
    

# my_lll is a standard implementation of the LLL algorithm

import my_lll HOST = "roasted-chal.firebird.sh" PORT = 36018 NUM_SAMPLES = 25 K = 10**40 def solve(): s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) s.connect((HOST, PORT))

```plaintext
# Select Exponent Mode
while b"Oracle type: " not in s.recv(4096): pass
s.sendall(b"exponent\n")
while b"Guess your flag: " not in s.recv(4096): pass
print("[*] Collecting samples to recover N...")
samples = []
total_score = 0

# 1. Collect incorrect samples
for _ in range(NUM_SAMPLES):
    s.sendall(b"IMPOSSIBLE_FLAG\n")
    resp = b""
    while b"Guess your flag: " not in resp:
        resp += s.recv(4096)
    
    lines = resp.decode().split('\n')
    e_val = int([l for l in lines if "e =" in l][0].split("= ")[1])
    score_val = int([l for l in lines if "total_score =" in l][0].split("= ")[1])
    
    diff = score_val - total_score # Integer difference
    total_score = score_val
    samples.append((e_val, diff))
# 2. Build Lattice and run LLL
print("[*] Running LLL...")
matrix = []
for i in range(NUM_SAMPLES):
    row = [0] * (NUM_SAMPLES + 1)
    row[i] = 1
    row[NUM_SAMPLES] = samples[i][0] * K
    matrix.append(row)

reduced = my_lll.lll_reduction(matrix)

# 3. Recover N from relations
candidates = []
for row in reduced:
    if row[NUM_SAMPLES] == 0: # Valid relation sum(c_i * e_i) = 0
        coeffs = row[:NUM_SAMPLES]
        if all(c == 0 for c in coeffs): continue
        
        # Calculate X = prod(diff^c) - 1
        num, den = 1, 1
        for i, c in enumerate(coeffs):
            if c > 0: num *= (samples[i][1] ** int(c))
            elif c < 0: den *= (samples[i][1] ** int(-c))
        
        val = abs(num - den)
        if val > 0: candidates.append(val)
        
N = candidates[0]
for c in candidates[1:]:
    N = gcd(N, c)
    
# Remove small factors
for small in [2, 3, 5, 7]:
    while N % small == 0: N //= small
        
print(f"[+] Recovered N (bits: {N.bit_length()}): {N}")
# 4. Brute force flag
# Reference sample (known incorrect)
ref_e, ref_diff = samples[0]
ref_diff %= N

flag = "firebird{Kn0w1ng_7h3_Xpon3n7_15_3n0ugh_70_f1nd_"
charset = string.printable.strip()

print(f"[*] Resuming flag search: {flag}")

while not flag.endswith("}"):
    # Use a sliding window for the guess to keep length valid
    prefix = flag[-14:] if len(flag) >= 14 else flag
    
    for char in charset:
        guess = prefix + char
        s.sendall(f"{guess}\n".encode())
        
        resp = b""
        while b"Guess your flag: " not in resp:
            resp += s.recv(4096)
            
        lines = resp.decode().split('\n')
        e_val = int([l for l in lines if "e =" in l][0].split("= ")[1])
        new_score = int([l for l in lines if "total_score =" in l][0].split("= ")[1])
        
        term = (new_score - total_score) % N
        total_score = new_score
        
        # Check: term^ref_e == ref_diff^e (mod N)
        # If equal -> multiplier was -1 (Incorrect)
        # If not equal -> multiplier was 2 (Correct)
        
        lhs = pow(term, ref_e, N)
        rhs = pow(ref_diff, e_val, N)
        
        if lhs != rhs:
            print(f"[+] Found: {char}")
            flag += char
            break
            
print(f"[SUCCESS] Flag: {flag}")
```

if name == "main": solve() The Flag After running the solver, we successfully recover the complete flag: firebird{Kn0w1ng_7h3_Xpon3n7_15_3n0ugh_70_f1nd_N}