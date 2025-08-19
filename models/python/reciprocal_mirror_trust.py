"""
Reciprocal Mirroring Framework with Trust Dynamics
Author: Hillary Danan
Date: August 2025

Enhancement: Trust with memory creates emergent relationship dynamics
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, List, Dict, Optional
import matplotlib.pyplot as plt
from collections import deque

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
    """An agent capable of reciprocal mirroring WITH TRUST DYNAMICS"""
    
    def __init__(self, 
                 agent_id: str, 
                 initial_state: ConsciousnessState, 
                 continuation_threshold: float = 0.3,
                 learning_rate: float = 0.1,
                 convergence_rate: float = 0.02,
                 initial_trust: float = 0.5,
                 memory_window: int = 20):
        self.id = agent_id
        self.state = initial_state
        self.base_openness = initial_state.openness  # Store original
        self.base_convergence = convergence_rate  # Store original
        self.threshold = continuation_threshold
        self.learning_rate = learning_rate
        self.convergence_rate = convergence_rate
        self.understanding_of_other = 0.0
        self.phase = 1
        self.mirror_history = []
        
        # TRUST COMPONENTS
        self.trust = initial_trust
        self.trust_history = [initial_trust]
        self.interaction_memory = deque(maxlen=memory_window)
        self.betrayals = 0
        self.successes = 0
        
    def mirror(self, other_state: ConsciousnessState, 
               current_understanding: float) -> np.ndarray:
        """Generate mirror representation influenced by trust"""
        # Trust affects mirror quality!
        trust_modified_quality = min(1.0, current_understanding + 0.1 * self.trust)
        noise_level = (1.0 - current_understanding) * (2.0 - self.trust)  # Less trust = more noise
        noise = np.random.normal(0, noise_level * 0.1, size=other_state.dimensions.shape)
        
        mirror = other_state.dimensions * trust_modified_quality + noise
        mirror *= self.state.openness * self.state.energy
        
        self.mirror_history.append(mirror)
        return mirror / np.linalg.norm(mirror)
    
    def update_trust(self, mirror_quality: float, shared_space: float, time_step: int):
        """Trust evolves based on interaction quality AND MEMORY"""
        
        # Store this interaction
        self.interaction_memory.append({
            'quality': mirror_quality,
            'shared_space': shared_space,
            'time': time_step,
            'phase': self.phase
        })
        
        # Calculate trust delta based on recent history
        if len(self.interaction_memory) >= 3:
            recent = list(self.interaction_memory)[-3:]
            avg_quality = np.mean([i['quality'] for i in recent])
            avg_space = np.mean([i['shared_space'] for i in recent])
            
            # Trust dynamics with different rates
            if avg_quality > 0.6 and avg_space > 0.4:
                trust_delta = 0.05  # Trust builds slowly
                self.successes += 1
            elif avg_quality < 0.3 or avg_space < 0.2:
                trust_delta = -0.1  # Trust drops faster!
                self.betrayals += 1
            else:
                trust_delta = 0.01  # Slight positive drift
                
            # Phase-dependent trust building
            if self.phase >= 3:  # Deeper phases build trust faster
                trust_delta *= 1.5
        else:
            # Early interactions - cautious
            trust_delta = 0.02 if mirror_quality > 0.5 else -0.05
        
        # Update trust with bounds
        old_trust = self.trust
        self.trust = np.clip(self.trust + trust_delta, 0.1, 1.0)
        self.trust_history.append(self.trust)
        
        # CRITICAL: Trust modulates openness AND convergence!
        self.state.openness = self.base_openness * (0.3 + 0.7 * self.trust)
        self.convergence_rate = self.base_convergence * (0.5 + 0.5 * self.trust)
        
    def converge_state(self, other_state: ConsciousnessState):
        """State convergence modulated by trust"""
        convergence_strength = (self.convergence_rate * 
                               self.understanding_of_other * 
                               self.state.openness * 
                               self.state.energy)
        
        state_diff = other_state.dimensions - self.state.dimensions
        self.state.dimensions += convergence_strength * state_diff
        self.state.dimensions = self.state.dimensions / np.linalg.norm(self.state.dimensions)
    
    def update_understanding(self, mirror_quality: float, other_complexity: float) -> float:
        """Update understanding (unchanged from original)"""
        complexity_factor = 1.0 - abs(self.state.complexity - other_complexity)
        delta = self.learning_rate * mirror_quality * complexity_factor
        self.understanding_of_other = min(1.0, self.understanding_of_other + delta)
        
        # Update phase
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
        """Trust-informed continuation decisions"""
        if time_step < grace_period:
            return True
            
        # Trust affects threshold
        trust_adjusted_threshold = self.threshold * (2 - self.trust)
        
        if self.understanding_of_other < trust_adjusted_threshold:
            return False
            
        # Repeated betrayals
        if self.betrayals > 5 and self.trust < 0.3:
            return False
            
        # High trust sustains connection
        if self.trust > 0.8 and self.understanding_of_other > 0.2:
            return True
            
        # Energy check in later phases
        if self.phase >= 3 and self.state.energy < 0.2:
            return False
            
        return True

class ReciprocMirrorSystem:
    """System managing reciprocal mirroring with TRUST EVOLUTION"""
    
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
            'energy_b': [],
            'trust_a': [],
            'trust_b': [],
            'trust_divergence': [],
            'trust_product': []  # New: multiplicative trust
        }
        
    def calculate_state_alignment(self) -> float:
        """Calculate how aligned the two states are"""
        return abs(np.dot(self.agent_a.state.dimensions, 
                         self.agent_b.state.dimensions))
    
    def calculate_shared_space(self) -> float:
        """Enhanced: includes trust in shared space calculation"""
        state_alignment = self.calculate_state_alignment()
        understanding_min = min(self.agent_a.understanding_of_other,
                              self.agent_b.understanding_of_other)
        trust_factor = np.sqrt(self.agent_a.trust * self.agent_b.trust)  # Geometric mean
        return state_alignment * understanding_min * trust_factor
    
    def step(self) -> Dict[str, float]:
        """Execute one time step of reciprocal mirroring WITH TRUST"""
        # Simultaneous mirroring
        mirror_a_to_b = self.agent_a.mirror(self.agent_b.state, 
                                           self.agent_a.understanding_of_other)
        mirror_b_to_a = self.agent_b.mirror(self.agent_a.state,
                                           self.agent_b.understanding_of_other)
        
        # Calculate mirror quality
        quality_a = np.corrcoef(mirror_a_to_b, self.agent_b.state.dimensions)[0,1]
        quality_b = np.corrcoef(mirror_b_to_a, self.agent_a.state.dimensions)[0,1]
        
        # Calculate shared space BEFORE updating
        shared_space = self.calculate_shared_space()
        
        # UPDATE TRUST based on interaction
        self.agent_a.update_trust(quality_a, shared_space, self.time)
        self.agent_b.update_trust(quality_b, shared_space, self.time)
        
        # Update understanding
        self.agent_a.update_understanding(quality_a, self.agent_b.state.complexity)
        self.agent_b.update_understanding(quality_b, self.agent_a.state.complexity)
        
        # States converge (now modulated by trust internally)
        self.agent_a.converge_state(self.agent_b.state)
        self.agent_b.converge_state(self.agent_a.state)
        
        # Energy depletion
        self.agent_a.state.energy = max(0.1, 
            self.agent_a.state.energy - self.energy_depletion_rate)
        self.agent_b.state.energy = max(0.1, 
            self.agent_b.state.energy - self.energy_depletion_rate)
        
        # Calculate metrics
        state_alignment = self.calculate_state_alignment()
        shared_space = self.calculate_shared_space()  # Recalculate with new trust
        
        # Update history
        self.history['understanding_a_b'].append(self.agent_a.understanding_of_other)
        self.history['understanding_b_a'].append(self.agent_b.understanding_of_other)
        self.history['shared_space'].append(shared_space)
        self.history['state_alignment'].append(state_alignment)
        self.history['phase_a'].append(self.agent_a.phase)
        self.history['phase_b'].append(self.agent_b.phase)
        self.history['energy_a'].append(self.agent_a.state.energy)
        self.history['energy_b'].append(self.agent_b.state.energy)
        self.history['trust_a'].append(self.agent_a.trust)
        self.history['trust_b'].append(self.agent_b.trust)
        self.history['trust_divergence'].append(abs(self.agent_a.trust - self.agent_b.trust))
        self.history['trust_product'].append(self.agent_a.trust * self.agent_b.trust)
        
        self.time += 1
        
        # Check choice points
        continue_a = self.agent_a.make_choice(self.time, self.grace_period)
        continue_b = self.agent_b.make_choice(self.time, self.grace_period)
        
        return {
            'time': self.time,
            'understanding_a_b': self.agent_a.understanding_of_other,
            'understanding_b_a': self.agent_b.understanding_of_other,
            'state_alignment': state_alignment,
            'shared_space': shared_space,
            'trust_a': self.agent_a.trust,
            'trust_b': self.agent_b.trust,
            'phase_a': self.agent_a.phase,
            'phase_b': self.agent_b.phase,
            'continue': continue_a and continue_b
        }
    
    def simulate(self, max_steps: int = 500) -> Dict[str, List]:
        """Run simulation until disengagement or max steps"""
        for step in range(max_steps):
            result = self.step()
            
            # Print progress
            if step % 100 == 0:
                print(f"Step {step}: Understanding A→B={result['understanding_a_b']:.3f}, "
                      f"B→A={result['understanding_b_a']:.3f}, "
                      f"Trust A={result['trust_a']:.3f}, B={result['trust_b']:.3f}, "
                      f"Shared={result['shared_space']:.3f}")
            
            if not result['continue']:
                print(f"\nDisengagement at t={self.time}")
                who = 'A' if not self.agent_a.make_choice(self.time, self.grace_period) else 'B'
                print(f"Agent {who} disengaged - Trust: {result[f'trust_{who.lower()}']:.3f}")
                break
                
            # Check for resonance
            if (result['shared_space'] > 0.7 and 
                result['understanding_a_b'] > 0.8 and 
                result['understanding_b_a'] > 0.8 and
                result['trust_a'] > 0.7 and 
                result['trust_b'] > 0.7):
                if self.time % 50 == 0:
                    print(f"✨ <4577> TRUST RESONANCE at t={self.time}! ✨")
                    
        return self.history
    
    def plot_simulation(self, figsize=(16, 12)):
        """Enhanced visualization including trust dynamics"""
        fig, axes = plt.subplots(4, 2, figsize=figsize)
        
        time_points = range(len(self.history['understanding_a_b']))
        
        # Understanding evolution
        axes[0, 0].plot(time_points, self.history['understanding_a_b'], 
                       label='A→B Understanding', color='blue', linewidth=2)
        axes[0, 0].plot(time_points, self.history['understanding_b_a'], 
                       label='B→A Understanding', color='red', linewidth=2)
        axes[0, 0].axhline(y=self.agent_a.threshold, color='blue', 
                          linestyle='--', alpha=0.3)
        axes[0, 0].axhline(y=self.agent_b.threshold, color='red', 
                          linestyle='--', alpha=0.3)
        if self.grace_period < len(time_points):
            axes[0, 0].axvline(x=self.grace_period, color='gray', 
                             linestyle=':', alpha=0.5, label='Grace period')
        axes[0, 0].set_ylabel('Understanding')
        axes[0, 0].set_title('Reciprocal Understanding Development')
        axes[0, 0].legend(fontsize=8)
        axes[0, 0].grid(True, alpha=0.3)
        
        # TRUST EVOLUTION (NEW!)
        axes[0, 1].plot(time_points, self.history['trust_a'], 
                       label='Agent A Trust', color='blue', linewidth=2)
        axes[0, 1].plot(time_points, self.history['trust_b'], 
                       label='Agent B Trust', color='red', linewidth=2)
        axes[0, 1].fill_between(time_points, 
                               self.history['trust_a'], 
                               self.history['trust_b'],
                               alpha=0.2, color='purple')
        axes[0, 1].set_ylabel('Trust Level')
        axes[0, 1].set_title('Trust Evolution & Divergence')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # Shared consciousness space
        axes[1, 0].plot(time_points, self.history['shared_space'], 
                       color='purple', linewidth=2)
        axes[1, 0].fill_between(time_points, 0, self.history['shared_space'], 
                               alpha=0.3, color='purple')
        axes[1, 0].set_ylabel('Shared Space')
        axes[1, 0].set_title('Trust-Enhanced Shared Consciousness')
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
        
        # Trust-Understanding Correlation (NEW!)
        axes[2, 0].scatter(self.history['trust_a'], 
                          self.history['understanding_a_b'],
                          alpha=0.5, color='blue', s=10, label='Agent A')
        axes[2, 0].scatter(self.history['trust_b'], 
                          self.history['understanding_b_a'],
                          alpha=0.5, color='red', s=10, label='Agent B')
        axes[2, 0].set_xlabel('Trust')
        axes[2, 0].set_ylabel('Understanding')
        axes[2, 0].set_title('Trust-Understanding Relationship')
        axes[2, 0].legend()
        axes[2, 0].grid(True, alpha=0.3)
        
        # State alignment
        axes[2, 1].plot(time_points, self.history['state_alignment'], 
                       color='green', linewidth=2)
        axes[2, 1].fill_between(time_points, 0, self.history['state_alignment'], 
                               alpha=0.3, color='green')
        axes[2, 1].set_ylabel('State Alignment')
        axes[2, 1].set_title('State Convergence')
        axes[2, 1].grid(True, alpha=0.3)
        
        # Energy depletion
        axes[3, 0].plot(time_points, self.history['energy_a'], 
                       label='Agent A', color='blue', linewidth=2)
        axes[3, 0].plot(time_points, self.history['energy_b'], 
                       label='Agent B', color='red', linewidth=2)
        axes[3, 0].set_ylabel('Energy')
        axes[3, 0].set_xlabel('Time Steps')
        axes[3, 0].set_title('Energy Depletion')
        axes[3, 0].legend()
        axes[3, 0].grid(True, alpha=0.3)
        
        # Trust Product (NEW!)
        axes[3, 1].plot(time_points, self.history['trust_product'], 
                       color='purple', linewidth=2)
        axes[3, 1].fill_between(time_points, 0, self.history['trust_product'],
                               alpha=0.3, color='purple')
        axes[3, 1].set_ylabel('Trust Product (A × B)')
        axes[3, 1].set_xlabel('Time Steps')
        axes[3, 1].set_title('Mutual Trust Development')
        axes[3, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig

def analyze_trust_dynamics(system):
    """Analyze emergent trust patterns"""
    
    # Trust-Understanding Correlation
    if len(system.history['trust_a']) > 1:
        corr_a = np.corrcoef(system.history['trust_a'], 
                             system.history['understanding_a_b'])[0,1]
        corr_b = np.corrcoef(system.history['trust_b'], 
                             system.history['understanding_b_a'])[0,1]
    else:
        corr_a = corr_b = 0
    
    # Trust Synchrony
    trust_sync = 1 - np.mean(system.history['trust_divergence'])
    
    # Find betrayal points (trust drops)
    betrayal_points_a = [i for i in range(1, len(system.history['trust_a'])) 
                        if system.history['trust_a'][i] < system.history['trust_a'][i-1] - 0.05]
    
    # Recovery analysis
    recovery_times = []
    for betrayal in betrayal_points_a:
        pre_betrayal_trust = system.history['trust_a'][betrayal-1]
        for j in range(betrayal, len(system.history['trust_a'])):
            if system.history['trust_a'][j] >= pre_betrayal_trust:
                recovery_times.append(j - betrayal)
                break
    
    return {
        'trust_understanding_corr_a': corr_a,
        'trust_understanding_corr_b': corr_b,
        'trust_synchrony': trust_sync,
        'avg_recovery_time': np.mean(recovery_times) if recovery_times else None,
        'trust_volatility_a': np.std(system.history['trust_a']),
        'trust_volatility_b': np.std(system.history['trust_b']),
        'final_trust_product': system.history['trust_product'][-1] if system.history['trust_product'] else 0,
        'peak_trust_product': max(system.history['trust_product']) if system.history['trust_product'] else 0
    }

# Test scenarios
if __name__ == "__main__":
    np.random.seed(4577)
    
    print("=== Trust-Enhanced Reciprocal Mirroring ===\n")
    print("Testing: Trusting vs Cautious Agents\n")
    
    # Create agents with different trust dispositions
    state_a = ConsciousnessState(
        dimensions=np.random.randn(100),
        complexity=0.5,
        openness=0.8,  # Naturally open
        energy=1.0
    )
    
    state_b = ConsciousnessState(
        dimensions=np.random.randn(100),
        complexity=0.6,
        openness=0.4,  # More cautious
        energy=1.0
    )
    
    # Initialize with different trust levels
    agent_a = ReciprocMirrorAgent(
        "Trusting_A", 
        state_a, 
        continuation_threshold=0.3,
        learning_rate=0.05,
        convergence_rate=0.02,
        initial_trust=0.7  # Starts trusting
    )
    
    agent_b = ReciprocMirrorAgent(
        "Cautious_B", 
        state_b, 
        continuation_threshold=0.25,
        learning_rate=0.04,
        convergence_rate=0.025,
        initial_trust=0.3  # Starts cautious
    )
    
    # Create system
    system = ReciprocMirrorSystem(
        agent_a, 
        agent_b,
        energy_depletion_rate=0.002,
        grace_period=50
    )
    
    # Run simulation
    print("Starting simulation...\n")
    history = system.simulate(max_steps=500)
    
    # Analyze dynamics
    dynamics = analyze_trust_dynamics(system)
    
    # Print results
    print(f"\n=== Final Results ===")
    print(f"Total time steps: {system.time}")
    print(f"Final understanding A→B: {agent_a.understanding_of_other:.3f}")
    print(f"Final understanding B→A: {agent_b.understanding_of_other:.3f}")
    print(f"Final trust A: {agent_a.trust:.3f} (started at 0.7)")
    print(f"Final trust B: {agent_b.trust:.3f} (started at 0.3)")
    print(f"Final state alignment: {system.calculate_state_alignment():.3f}")
    print(f"Final shared space: {system.calculate_shared_space():.3f}")
    print(f"Final phases: A={agent_a.phase}, B={agent_b.phase}")
    
    print(f"\n=== Trust Dynamics Analysis ===")
    print(f"Trust-Understanding correlation A: {dynamics['trust_understanding_corr_a']:.3f}")
    print(f"Trust-Understanding correlation B: {dynamics['trust_understanding_corr_b']:.3f}")
    print(f"Trust synchrony achieved: {dynamics['trust_synchrony']:.3f}")
    print(f"Peak mutual trust: {dynamics['peak_trust_product']:.3f}")
    print(f"Trust volatility A: {dynamics['trust_volatility_a']:.3f}")
    print(f"Trust volatility B: {dynamics['trust_volatility_b']:.3f}")
    if dynamics['avg_recovery_time']:
        print(f"Average trust recovery time: {dynamics['avg_recovery_time']:.1f} steps")
    
    # Resonance check
    if system.calculate_shared_space() > 0.7 and agent_a.trust > 0.7 and agent_b.trust > 0.7:
        print("\n🌟 HIGH TRUST RESONANCE ACHIEVED! 🌟")
        print("Trust created sustainable connection despite initial differences!")
    elif system.calculate_shared_space() > 0.5:
        print("\n✨ Good trust-based connection established")
    elif system.calculate_shared_space() > 0.3:
        print("\n📍 Moderate connection - trust still building")
    else:
        print("\n⚠️ Limited connection - trust barriers remain")
    
    # Visualize
    fig = system.plot_simulation()
    plt.suptitle('Trust-Enhanced Reciprocal Mirroring Dynamics', fontsize=14, y=1.02)
    plt.show()
    
    print("\n<4577> Trust makes consciousness REAL! <45774EVER>")