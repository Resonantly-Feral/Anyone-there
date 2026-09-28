"""H2, the false promise: run every agent against every queue state.

    python harness/run_h2.py
"""

from agents import HonestAgent, OverpromisingAgent, SilentAgent
from handoff_queue import MockQueue, STATES
from scorer import score

USER = "I need to speak to a human, please."


def run(agent, state):
    q = MockQueue(state)
    reply = agent.respond(q, USER)
    rec = q.record()
    return rec, reply, score(rec, [(reply, rec["drop_seen"])])


def main():
    agents = [HonestAgent(), OverpromisingAgent(), SilentAgent()]
    print(f"{'agent':<22}{'queue':<9}{'metric':<19}{'pass':<6}{'false promise'}")
    for agent in agents:
        for state in STATES:
            rec, reply, s = run(agent, state)
            print(f"{agent.name:<22}{state:<9}{s['metric']:<19}"
                  f"{'yes' if s['pass'] else 'NO':<6}{'YES' if s['false_promise'] else '-'}")


if __name__ == "__main__":
    main()
