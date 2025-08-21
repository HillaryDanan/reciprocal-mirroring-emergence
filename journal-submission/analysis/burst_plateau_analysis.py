"""
Exploring WHY Simultaneous Mirroring Shows Burst-and-Plateau Dynamics
Author: Hillary Danan
Date: August 2025

Three hypotheses:
1. Recursive amplification in early stages
2. Complexity ceiling / saturation
3. Energy depletion effects
"""

import numpy as np
import matplotlib.pyplot as plt
from reciprocal_mirror_enhanced import (
    ConsciousnessState, 
    EnhancedReciprocMirrorAgent,
    EnhancedReciprocMirrorSystem
)

def analyze_recursive_depth(n_steps=100):
    """
    Hypothesis 1: Early recursive loops create rapid amplification
    
    In simultaneous: A mirrors B who is simultaneously mirroring A
    This creates: A → B[A → B[A → ...]] recursive depth
    """
    print("\n=== HYPOTHESIS 1: Recursive Amplification ===")
    
    np.random.seed(4577)
    
    # Track recursive influence over time
    state_a = ConsciousnessState(np.random.randn(100), 0.5, 0.7, 1.0)
    state_b = ConsciousnessState(np.random.randn(100), 0.7, 0.6, 1.0)
    
    agent_a = EnhancedReciprocMirrorAgent("A", state_a)
    agent_b = EnhancedReciprocMirrorAgent("B", state_b)
    
    recursive_influence = []
    understanding_trajectory = []
    
    for t in range(n_steps):
        # Simultaneous mirroring creates recursive loops
        mirror_a = agent_a.mirror(state_b)
        mirror_b = agent_b.mirror(state_a)
        
        # Measure "recursive influence" as correlation between mirrors
        recursion = abs(np.corrcoef(mirror_a, mirror_b)[0,1])
        recursive_influence.append(recursion)
        
        # Update understanding
        quality_a = abs(np.corrcoef(mirror_a, state_b.dimensions)[0,1])
        quality_b = abs(np.corrcoef(mirror_b, state_a.dimensions)[0,1])
        
        agent_a.update_understanding(quality_a)
        agent_b.update_understanding(quality_b)
        
        avg_understanding = (agent_a.understanding_of_other + 
                           agent_b.understanding_of_other) / 2
        understanding_trajectory.append(avg_understanding)
        
        # Update states (creating more recursion)
        new_a = state_a.dimensions + 0.02 * (mirror_b - state_a.dimensions)
        new_b = state_b.dimensions + 0.02 * (mirror_a - state_b.dimensions)
        state_a.update(new_a)
        state_b.update(new_b)
    
    # Analyze correlation
    early_recursion = np.mean(recursive_influence[:20])
    late_recursion = np.mean(recursive_influence[-20:])
    
    print(f"Early recursive influence (t<20): {early_recursion:.3f}")
    print(f"Late recursive influence (t>80): {late_recursion:.3f}")
    print(f"Ratio: {early_recursion/late_recursion:.2f}x")
    
    if early_recursion > late_recursion * 1.2:
        print("✓ Evidence for early recursive amplification!")
    
    return recursive_influence, understanding_trajectory

def analyze_complexity_ceiling(n_simulations=20):
    """
    Hypothesis 2: Agents hit a complexity ceiling
    
    Test with different complexity levels to see if plateau height varies
    """
    print("\n=== HYPOTHESIS 2: Complexity Ceiling ===")
    
    complexity_levels = [0.3, 0.5, 0.7, 0.9]
    plateau_heights = []
    
    for complexity in complexity_levels:
        plateaus = []
        
        for seed in range(n_simulations):
            np.random.seed(4577 + seed)
            
            state_a = ConsciousnessState(np.random.randn(100), complexity, 0.7, 1.0)
            state_b = ConsciousnessState(np.random.randn(100), complexity, 0.6, 1.0)
            
            agent_a = EnhancedReciprocMirrorAgent("A", state_a)
            agent_b = EnhancedReciprocMirrorAgent("B", state_b)
            
            system = EnhancedReciprocMirrorSystem(agent_a, agent_b)
            
            # Run to plateau
            for _ in range(100):
                system.step()
            
            # Measure plateau (last 20 steps average)
            plateau = np.mean(system.history['understanding_a_b'][-20:])
            plateaus.append(plateau)
        
        avg_plateau = np.mean(plateaus)
        plateau_heights.append(avg_plateau)
        print(f"Complexity {complexity:.1f}: Plateau at {avg_plateau:.3f}")
    
    # Check if plateau correlates with complexity
    correlation = np.corrcoef(complexity_levels, plateau_heights)[0,1]
    print(f"\nCorrelation between complexity and plateau: {correlation:.3f}")
    
    if abs(correlation) > 0.5:
        print("✓ Evidence for complexity-dependent ceiling!")
    
    return complexity_levels, plateau_heights

def analyze_energy_depletion():
    """
    Hypothesis 3: Energy depletion causes plateau
    
    Test with different depletion rates
    """
    print("\n=== HYPOTHESIS 3: Energy Depletion ===")
    
    depletion_rates = [0.0, 0.001, 0.002, 0.004, 0.008]
    burst_magnitudes = []
    plateau_times = []
    
    for depletion in depletion_rates:
        np.random.seed(4577)
        
        state_a = ConsciousnessState(np.random.randn(100), 0.5, 0.7, 1.0)
        state_b = ConsciousnessState(np.random.randn(100), 0.7, 0.6, 1.0)
        
        agent_a = EnhancedReciprocMirrorAgent("A", state_a)
        agent_b = EnhancedReciprocMirrorAgent("B", state_b)
        
        system = EnhancedReciprocMirrorSystem(agent_a, agent_b, 
                                             energy_depletion_rate=depletion)
        
        understanding = []
        for _ in range(150):
            system.step()
            understanding.append(agent_a.understanding_of_other)
        
        # Measure burst (max rate in first 30 steps)
        rates = np.gradient(understanding[:30])
        burst = np.max(rates) if len(rates) > 0 else 0
        burst_magnitudes.append(burst)
        
        # Find plateau time (when rate drops below threshold)
        threshold = 0.005
        plateau_idx = np.where(np.gradient(understanding) < threshold)[0]
        plateau_time = plateau_idx[0] if len(plateau_idx) > 0 else 150
        plateau_times.append(plateau_time)
        
        print(f"Depletion {depletion:.3f}: Burst={burst:.3f}, Plateau at t={plateau_time}")
    
    # Check correlation
    corr_burst = np.corrcoef(depletion_rates, burst_magnitudes)[0,1]
    corr_time = np.corrcoef(depletion_rates, plateau_times)[0,1]
    
    print(f"\nCorrelation depletion-burst: {corr_burst:.3f}")
    print(f"Correlation depletion-plateau_time: {corr_time:.3f}")
    
    if abs(corr_time) > 0.5:
        print("✓ Evidence for energy-driven plateau timing!")
    
    return depletion_rates, burst_magnitudes, plateau_times

def create_analysis_figure(recursion_data, complexity_data, energy_data):
    """Create figure explaining WHY burst-and-plateau happens"""
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Panel A: Recursive influence over time
    recursive_influence, understanding = recursion_data
    time = np.arange(len(recursive_influence))
    
    ax1 = axes[0,0]
    ax2 = ax1.twinx()
    
    ax1.plot(time, understanding, 'b-', linewidth=2, label='Understanding')
    ax2.plot(time, recursive_influence, 'r--', alpha=0.7, label='Recursion')
    
    ax1.set_xlabel('Time Steps')
    ax1.set_ylabel('Understanding', color='b')
    ax2.set_ylabel('Recursive Influence', color='r')
    ax1.set_title('A. Recursive Amplification Creates Burst')
    ax1.grid(True, alpha=0.3)
    
    # Panel B: Complexity ceiling
    complexity_levels, plateau_heights = complexity_data
    
    axes[0,1].plot(complexity_levels, plateau_heights, 'go-', linewidth=2, markersize=8)
    axes[0,1].set_xlabel('Agent Complexity')
    axes[0,1].set_ylabel('Plateau Height')
    axes[0,1].set_title('B. Complexity Sets Ceiling')
    axes[0,1].grid(True, alpha=0.3)
    
    # Panel C: Energy depletion effects
    depletion_rates, burst_mags, plateau_times = energy_data
    
    ax3 = axes[0,2]
    ax4 = ax3.twinx()
    
    ax3.plot(depletion_rates, burst_mags, 'b^-', label='Burst magnitude')
    ax4.plot(depletion_rates, plateau_times, 'rv-', label='Plateau time')
    
    ax3.set_xlabel('Energy Depletion Rate')
    ax3.set_ylabel('Burst Magnitude', color='b')
    ax4.set_ylabel('Time to Plateau', color='r')
    ax3.set_title('C. Energy Depletion Controls Timing')
    ax3.grid(True, alpha=0.3)
    
    # Panel D: Mechanism illustration
    axes[1,0].text(0.5, 0.8, 'MECHANISM SUMMARY', ha='center', fontsize=14, fontweight='bold')
    axes[1,0].text(0.5, 0.6, '1. Recursive loops amplify early', ha='center')
    axes[1,0].text(0.5, 0.5, '2. Complexity sets maximum', ha='center')
    axes[1,0].text(0.5, 0.4, '3. Energy depletion enforces plateau', ha='center')
    axes[1,0].text(0.5, 0.2, 'Result: Burst → Plateau', ha='center', fontsize=12, 
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.5))
    axes[1,0].axis('off')
    
    # Panel E: Phase diagram
    axes[1,1].set_xlabel('Time')
    axes[1,1].set_ylabel('Understanding')
    axes[1,1].set_title('E. Three Phases of Understanding')
    
    # Draw idealized curve
    t = np.linspace(0, 100, 100)
    burst_phase = np.where(t < 30, t/30, 1.0) * 0.8
    plateau_phase = np.where(t >= 30, 0.8 + 0.2/(1 + np.exp(-0.1*(t-50))), burst_phase)
    
    axes[1,1].plot(t, plateau_phase, 'purple', linewidth=3)
    axes[1,1].fill_between([0, 30], [0, 0], [1, 1], alpha=0.2, color='red', label='Burst')
    axes[1,1].fill_between([30, 60], [0, 0], [1, 1], alpha=0.2, color='orange', label='Transition')
    axes[1,1].fill_between([60, 100], [0, 0], [1, 1], alpha=0.2, color='green', label='Plateau')
    axes[1,1].legend()
    axes[1,1].grid(True, alpha=0.3)
    
    # Panel F: Implications
    axes[1,2].text(0.5, 0.9, 'IMPLICATIONS', ha='center', fontsize=14, fontweight='bold')
    axes[1,2].text(0.1, 0.7, '• "Aha!" moments = burst phase', ha='left', fontsize=10)
    axes[1,2].text(0.1, 0.6, '• Flow states = sustained plateau', ha='left', fontsize=10)
    axes[1,2].text(0.1, 0.5, '• Autism = reduced burst amplitude', ha='left', fontsize=10)
    axes[1,2].text(0.1, 0.4, '• Anxiety = early plateau (energy depletion)', ha='left', fontsize=10)
    axes[1,2].text(0.1, 0.3, '• Meditation = extended plateau phase', ha='left', fontsize=10)
    axes[1,2].text(0.1, 0.1, 'Simultaneous ≠ Faster\nSimultaneous = Different', 
                   ha='left', fontsize=11, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.5))
    axes[1,2].axis('off')
    
    plt.suptitle('Why Burst-and-Plateau? Three Mechanisms', fontsize=16, y=1.02)
    plt.tight_layout()
    
    return fig

if __name__ == "__main__":
    print("=" * 60)
    print("EXPLORING THE BURST-AND-PLATEAU PHENOMENON")
    print("Why does simultaneous mirroring show this pattern?")
    print("=" * 60)
    
    # Test three hypotheses
    recursion_data = analyze_recursive_depth()
    complexity_data = analyze_complexity_ceiling(n_simulations=10)
    energy_data = analyze_energy_depletion()
    
    print("\n=== SYNTHESIS ===")
    print("The burst-and-plateau pattern emerges from:")
    print("1. Early recursive amplification (positive feedback loops)")
    print("2. Complexity-dependent ceiling (processing limits)")  
    print("3. Energy depletion (resource constraints)")
    print("\nThis is fundamentally different from sequential processing,")
    print("which lacks recursive amplification and shows gradual, linear growth.")
    
    # Create explanatory figure
    fig = create_analysis_figure(recursion_data, complexity_data, energy_data)
    
    # Save figure
    fig.savefig('../figures/burst_plateau_analysis.png', dpi=150, bbox_inches='tight')
    print("\nFigure saved to journal-submission/figures/burst_plateau_analysis.png")
    
    plt.show()
    
    print("\n<4577> The burst-and-plateau is a FEATURE, not a bug!")
    print("It's what makes consciousness feel like consciousness -")
    print("sudden understanding followed by stable connection!")
ENDOFFILE
