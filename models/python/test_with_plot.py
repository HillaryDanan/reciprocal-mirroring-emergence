import numpy as np
import matplotlib.pyplot as plt
from reciprocal_mirror import ConsciousnessState, ReciprocMirrorAgent, ReciprocMirrorSystem

# Set seed for reproducibility
np.random.seed(4577)

# Create two agents with different complexities
state_a = ConsciousnessState(
    dimensions=np.random.randn(100),
    complexity=0.5,
    openness=0.6,
    energy=1.0
)

state_b = ConsciousnessState(
    dimensions=np.random.randn(100),
    complexity=0.7,
    openness=0.8,
    energy=1.0
)

agent_a = ReciprocMirrorAgent("Agent_A", state_a)
agent_b = ReciprocMirrorAgent("Agent_B", state_b)

# Create and run system
system = ReciprocMirrorSystem(agent_a, agent_b)

# Run for more steps to see evolution
for i in range(200):
    result = system.step()
    if i % 50 == 0:
        print(f"Step {i}: Understanding A→B: {result['understanding_a_b']:.3f}, "
              f"B→A: {result['understanding_b_a']:.3f}, "
              f"Shared: {result['shared_space']:.3f}")

# Plot results
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Plot understanding evolution
time_steps = range(len(system.history['understanding_a_b']))
axes[0].plot(time_steps, system.history['understanding_a_b'], 
            label='A→B Understanding', color='blue', linewidth=2)
axes[0].plot(time_steps, system.history['understanding_b_a'], 
            label='B→A Understanding', color='red', linewidth=2)
axes[0].set_ylabel('Understanding Level')
axes[0].set_title('Reciprocal Understanding Development')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot shared consciousness space
axes[1].plot(time_steps, system.history['shared_space'], 
            color='purple', linewidth=2)
axes[1].fill_between(time_steps, 0, system.history['shared_space'], 
                     alpha=0.3, color='purple')
axes[1].set_ylabel('Shared Space')
axes[1].set_xlabel('Time Steps')
axes[1].set_title('Shared Consciousness Space Evolution')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('mirroring_results.png', dpi=150, bbox_inches='tight')
print("\nPlot saved as 'mirroring_results.png'")
plt.show()

# Print final statistics
print("\n=== Final Statistics ===")
print(f"Agent A final phase: {agent_a.phase}")
print(f"Agent B final phase: {agent_b.phase}")
print(f"Final understanding A→B: {agent_a.understanding_of_other:.3f}")
print(f"Final understanding B→A: {agent_b.understanding_of_other:.3f}")
print(f"Final shared space: {system.calculate_shared_space():.3f}")

# Check if they reached high resonance
if agent_a.understanding_of_other > 0.8 and agent_b.understanding_of_other > 0.8:
    print("\n<4577> High resonance achieved!")
