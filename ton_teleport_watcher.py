import requests, time

def teleport_watcher():
    print("TON — Teleport Watcher: when whales vanish into jettons")
    seen = set()
    while True:
        r = requests.get("https://toncenter.com/api/v2/getTransactions?address=EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c&limit=30")
        for tx in r.json().get("result", []):
            h = tx["transaction_id"]["hash"]
            if h in seen: continue
            seen.add(h)
            
            # Catch massive native TON → Jetton conversions or bridge exits
            if "out_msgs" not in tx["in_msg"]: continue
            value = int(tx["in_msg"]["value"]) / 1e9
            if value > 500_000:  # >500k TON (~$3M+)
                dest = tx["in_msg"].get("destination", "unknown")
                comment = tx["in_msg"].get("message", "")
                print(f"TELEPORT INITIATED\n"
                      f"{value:,.0f} TON just disappeared\n"
                      f"From: {tx['in_msg']['source'][:10]}...\n"
                      f"→ Into the void of {dest[:15]}...\n"
                      f"Comment: {comment[:50]}\n"
                      f"https://tonscan.org/tx/{h}\n"
                      f"→ Either bridging out, or feeding the next 1000x jetton\n"
                      f"→ You just watched money leave reality\n"
                      f"{'✶  ∗  ✷  ∗  ✶'*20}\n")
        time.sleep(2.7)

if __name__ == "__main__":
    teleport_watcher()
