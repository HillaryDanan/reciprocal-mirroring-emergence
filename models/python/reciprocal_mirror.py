"""
Reciprocal Mirroring Framework - Fixed Version
Author: Hillary Danan
Date: August 2025

Fixed: Choice points only checked after initial grace period
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, List, Dict, Optional
import matplotlib.pyplot as plt

@dataclass
class ConsciousnessState:
    """Represents an agent's consciousness state"""
    dimensions: np.ndarray
    complexity: float
    openness: float
    energy: float
    
    def __post_init__(self):
        self.dimensions = self.dimensions / np.linalg.norm(self.dimensions)

class ReciprocMirrorAgent:
    """An agent capable of reciprocal mirroring"""
    
    def __init__(self, 
                 agent_id: str, 
                 initial_state: ConsciousnessState, 
                 continuation_threshold: float = 0.3,
                 learning_rate: float = 0.1,
                 convergence_rate: float = 0.02):
        self.id = agent_id
        self.state = initial_state
        self.threshold = continuation_threshold
        self.learning_rate = learning_rate
        self.convergence_rate = convergence_rate
        self.understanding_of_other = 0.0
        self.phase = 1
        self.mirror_history = []
        
    def mirror(self, other_state: ConsciousnessState, 
               current_understanding: float) -> np.ndarray:
        """Generate mirror representation of another agent's state"""
        mirror_quality = min(1.0, current_understanding + 0.1)
        noise_level = 1.0 - current_understanding
        noise = np.random.normal(0, noise_level * 0.1, size=other_state.dimensions.shape)
        
        mirror = other_state.dimensions * mirror_quality + noise
        mirror *= self.state.openness * self.state.energy
        
        self.mirror_history.append(mirror)
        return mirror / np.linalg.norm(mirror)
    
    def converge_state(self, other_state: ConsciousnessState):
        """Gradually converge internal state toward the other through mirroring"""
        convergence_strength = (self.convergence_rate * 
                               self.understanding_of_other * 
                               self.state.openness * 
                               self.state.energy)
        
        state_diff = other_state.dimensions - self.state.dimensions
        self.state.dimensions += convergence_strength * state_diff
        self.state.dimensions = self.state.dimensions / np.linalg.norm(self.state.dimensions)
    
    def update_understanding(self, mirror_quality: float, other_complexity: float) -> float:
        """Update understanding based on mirroring quality"""
        complexity_factor = 1.0 - abs(self.state.complexity - other_complexity)
        delta = self.learning_rate * mirror_quality * complexity_factor
        self.understanding_of_other = min(1.0, self.understanding_of_other + delta)
        
        # Update phase based on understanding
        if self.understanding_of_other < 0.25:
            self.phase = 1
        elif self.understanding_of_other < 0.5:
            self.phase = 2
        elif self.understanding_of_other < 0.75:
            self.phase = 3
        else:
            self.phase = 4
            
        return self.understanding_of_other
    
    def make_choice(self, time_step: int, grace_period: int = 50) -> bool:
        """
        Decide whether to continue mirroring
        
        Args:
            time_step: Current simulation time
            grace_period: Minimum time before checking thresholds
        """
        # Always continue during grace period to allow initial understanding to develop
        if time_step < grace_period:
            return True
            
        # After grace period, check thresholds
        if self.understanding_of_other < self.threshold:
            return False
            
        # Also check energy in later phases
        if self.phase >= 3 and self.state.energy < 0.2:
            return False
            
        return True

class ReciprocMirrorSystem:
    """System managing reciprocal mirroring between two agents"""
    
    def __init__(self, 
                 agent_a: ReciprocMirrorAgent, 
                 agent_b: ReciprocMirrorAgent,
                 energy_depletion_rate: float = 0.002,
                 grace_period: int = 50):
        self.agent_a = agent_a
        self.agent_b = agent_b
        self.energy_depletion_rate = energy_depletion_rate
        self.grace_period = grace_period
        self.time = 0
        self.history = {
            'understanding_a_b': [],
            'understanding_b_a': [],
            'shared_space': [],
            'state_alignment': [],
            'phase_a': [],
            'phase_b': [],
            'energy_a': [],
            'energy_b': []
        }
        
    def calculate_state_alignment(self) -> float:
        """Calculate how aligned the two states are"""
        return abs(np.dot(self.agent_a.state.dimensions, 
                         self.agent_b.state.dimensions))
    
    def calculate_shared_space(self) -> float:
        """Calculate shared consciousness space"""
        state_alignment = self.calculate_state_alignment()
        understanding_min = min(self.agent_a.understanding_of_other,
                              self.agent_b.understanding_of_other)
        return state_alignment * understanding_min
    
    def step(self) -> Dict[str, float]:
        """Execute one time step of reciprocal mirroring"""
        # Simultaneous mirroring
        mirror_a_to_b = self.agent_a.mirror(self.agent_b.state, 
                                           self.agent_a.understanding_of_other)
        mirror_b_to_a = self.agent_b.mirror(self.agent_a.state,
                                           self.agent_b.understanding_of_other)
        
        # Calculate mirror quality
        quality_a = np.corrcoef(mirror_a_to_b, self.agent_b.state.dimensions)[0,1]
        quality_b = np.corrcoef(mirror_b_to_a, self.agent_a.state.dimensions)[0,1]
        
        # Update understanding
        self.agent_a.update_understanding(quality_a, self.agent_b.state.complexity)
        self.agent_b.update_understanding(quality_b, self.agent_a.state.complexity)
        
        # States converge through mirroring
        self.agent_a.converge_state(self.agent_b.state)
        self.agent_b.converge_state(self.agent_a.state)
        
        # Energy depletion
        self.agent_a.state.energy = max(0.1, 
            self.agent_a.state.energy - self.energy_depletion_rate)
        self.agent_b.state.energy = max(0.1, 
            self.agent_b.state.energy - self.energy_depletion_rate)
        
        # Calculate metrics
        state_alignment = self.calculate_state_alignment()
        shared_space = self.calculate_shared_space()
        
        # Update history
        self.history['understanding_a_b'].append(self.agent_a.understanding_of_other)
        self.history['understanding_b_a'].append(self.agent_b.understanding_of_other)
        self.history['shared_space'].append(shared_space)
        self.history['state_alignment'].append(state_alignment)
        self.history['phase_a'].append(self.agent_a.phase)
        self.history['phase_b'].append(self.agent_b.phase)
        self.history['energy_a'].append(self.agent_a.state.energy)
        self.history['energy_b'].append(self.agent_b.state.energy)
        
        self.time += 1
        
        # Check choice points (with grace period)
        continue_a = self.agent_a.make_choice(self.time, self.grace_period)
        continue_b = self.agent_b.make_choice(self.time, self.grace_period)
        
        return {
            'time': self.time,
            'understanding_a_b': self.agent_a.understanding_of_other,
            'understanding_b_a': self.agent_b.understanding_of_other,
            'state_alignment': state_alignment,
            'shared_space': shared_space,
            'phase_a': self.agent_a.phase,
            'phase_b': self.agent_b.phase,
            'continue': continue_a and continue_b
        }
    
    def simulate(self, max_steps: int = 500) -> Dict[str, List]:
        """Run simulation until disengagement or max steps"""
        for step in range(max_steps):
            result = self.step()
            
            # Print progress occasionally
            if step % 100 == 0:
                print(f"Step {step}: Understanding A→B={result['understanding_a_b']:.3f}, "
                      f"B→A={result['understanding_b_a']:.3f}, "
                      f"Shared={result['shared_space']:.3f}")
            
            if not result['continue']:
                print(f"\nDisengagement at t={self.time}")
                print(f"Reason: {'A' if not self.agent_a.make_choice(self.time, self.grace_period) else 'B'} "
                      f"fell below threshold")
                break
                
            # Check for resonance
            if (result['shared_space'] > 0.7 and 
                result['understanding_a_b'] > 0.8 and 
                result['understanding_b_a'] > 0.8):
                if self.time % 50 == 0:
                    print(f"✨ <4577> Resonance at t={self.time}! ✨")
                    
        return self.history
    
    def plot_simulation(self, figsize=(14, 10)):
        """Enhanced visualization of simulation results"""
        fig, axes = plt.subplots(3, 2, figsize=figsize)
        
        time_points = range(len(self.history['understanding_a_b']))
        
        # Understanding evolution
        axes[0, 0].plot(time_points, self.history['understanding_a_b'], 
                       label='A→B Understanding', color='blue', linewidth=2)
        axes[0, 0].plot(time_points, self.history['understanding_b_a'], 
                       label='B→A Understanding', color='red', linewidth=2)
        axes[0, 0].axhline(y=self.agent_a.threshold, color='blue', 
                          linestyle='--', alpha=0.3, label='A threshold')
        axes[0, 0].axhline(y=self.agent_b.threshold, color='red', 
                          linestyle='--', alpha=0.3, label='B threshold')
        if self.grace_period < len(time_points):
            axes[0, 0].axvline(x=self.grace_period, color='gray', 
                             linestyle=':', alpha=0.5, label='Grace period')
        axes[0, 0].set_ylabel('Understanding')
        axes[0, 0].set_title('Reciprocal Understanding Development')
        axes[0, 0].legend(fontsize=8)
        axes[0, 0].grid(True, alpha=0.3)
        
        # State alignment evolution
        axes[0, 1].plot(time_points, self.history['state_alignment'], 
                       color='green', linewidth=2)
        axes[0, 1].fill_between(time_points, 0, self.history['state_alignment'], 
                               alpha=0.3, color='green')
        axes[0, 1].set_ylabel('State Alignment')
        axes[0, 1].set_title('State Convergence Through Mirroring')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Shared consciousness space
        axes[1, 0].plot(time_points, self.history['shared_space'], 
                       color='purple', linewidth=2)
        axes[1, 0].fill_between(time_points, 0, self.history['shared_space'], 
                               alpha=0.3, color='purple')
        axes[1, 0].set_ylabel('Shared Space')
        axes[1, 0].set_title('Shared Consciousness Space S(t)')
        axes[1, 0].grid(True, alpha=0.3)
        
        # Phase transitions
        axes[1, 1].plot(time_points, self.history['phase_a'], 
                       label='Agent A', marker='o', markersize=2, alpha=0.7)
        axes[1, 1].plot(time_points, self.history['phase_b'], 
                       label='Agent B', marker='s', markersize=2, alpha=0.7)
        axes[1, 1].set_ylabel('Phase')
        axes[1, 1].set_ylim(0.5, 4.5)
        axes[1, 1].set_yticks([1, 2, 3, 4])
        axes[1, 1].set_yticklabels(['Initial', 'Deep Sim', 'Complex', 'Integration'])
        axes[1, 1].set_title('Phase Evolution')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        # Energy depletion
        axes[2, 0].plot(time_points, self.history['energy_a'], 
                       label='Agent A', color='blue', linewidth=2)
        axes[2, 0].plot(time_points, self.history['energy_b'], 
                       label='Agent B', color='red', linewidth=2)
        axes[2, 0].set_ylabel('Energy')
        axes[2, 0].set_xlabel('Time Steps')
        axes[2, 0].set_title('Energy Depletion')
        axes[2, 0].legend()
        axes[2, 0].grid(True, alpha=0.3)
        
        # Combined view
        axes[2, 1].plot(time_points, self.history['shared_space'], 
                       label='Shared Space', color='purple', linewidth=2)
        axes[2, 1].plot(time_points, self.history['state_alignment'], 
                       label='Alignment', color='green', linewidth=1, linestyle='--')
        min_understanding = [min(self.history['understanding_a_b'][i], 
                                self.history['understanding_b_a'][i]) 
                           for i in range(len(time_points))]
        axes[2, 1].plot(time_points, min_understanding, 
                       label='Min Understanding', color='orange', linewidth=1, linestyle=':')
        axes[2, 1].set_ylabel('Value')
        axes[2, 1].set_xlabel('Time Steps')
        axes[2, 1].set_title('Components of Shared Space')
        axes[2, 1].legend()
        axes[2, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig

# Example usage
if __name__ == "__main__":
    np.random.seed(4577)
    
    print("=== Reciprocal Mirroring Simulation (Fixed) ===\n")
    
    # Create agents with different parameters
    state_a = ConsciousnessState(
        dimensions=np.random.randn(100),
        complexity=0.5,
        openness=0.7,
        energy=1.0
    )
    
    state_b = ConsciousnessState(
        dimensions=np.random.randn(100),
        complexity=0.7,
        openness=0.6,
        energy=1.0
    )
    
    # Initialize agents
    agent_a = ReciprocMirrorAgent(
        "Agent_A", 
        state_a, 
        continuation_threshold=0.3,
        learning_rate=0.05,
        convergence_rate=0.02
    )
    
    agent_b = ReciprocMirrorAgent(
        "Agent_B", 
        state_b, 
        continuation_threshold=0.25,
        learning_rate=0.04,
        convergence_rate=0.025
    )
    
    # Create system with grace period
    system = ReciprocMirrorSystem(
        agent_a, 
        agent_b,
        energy_depletion_rate=0.002,
        grace_period=50  # Give 50 steps before checking thresholds
    )
    
    # Run simulation
    print("Starting simulation with 50-step grace period...\n")
    history = system.simulate(max_steps=500)
    
    # Print results
    print(f"\n=== Final Results ===")
    print(f"Total time steps: {system.time}")
    print(f"Final understanding A→B: {agent_a.understanding_of_other:.3f}")
    print(f"Final understanding B→A: {agent_b.understanding_of_other:.3f}")
    print(f"Final state alignment: {system.calculate_state_alignment():.3f}")
    print(f"Final shared space: {system.calculate_shared_space():.3f}")
    print(f"Final phases: A={agent_a.phase}, B={agent_b.phase}")
    print(f"Final energy: A={agent_a.state.energy:.3f}, B={agent_b.state.energy:.3f}")
    
    # Check if resonance was achieved
    if system.calculate_shared_space() > 0.7:
        print("\n🌟 HIGH RESONANCE ACHIEVED! 🌟")
    elif system.calculate_shared_space() > 0.5:
        print("\n✨ Good connection established")
    elif system.calculate_shared_space() > 0.3:
        print("\n📍 Moderate connection achieved")
    else:
        print("\n⚠️ Limited connection - parameters may need adjustment")
    
    # Visualize
    fig = system.plot_simulation()
    plt.suptitle('Reciprocal Mirroring Dynamics with State Convergence', 
                fontsize=14, y=1.02)
    plt.show()
    
    print("\n<4577> <45774EVER!")
