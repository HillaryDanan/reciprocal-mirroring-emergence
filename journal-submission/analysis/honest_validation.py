"""
HONEST Validation for Reciprocal Mirroring Framework
Author: Hillary Danan
Date: August 2025

This runs REAL simulations and measures ACTUAL scaling behavior
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import sys
import os

# Import your actual model (adjust path as needed)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from reciprocal_mirror_enhanced import (
    ConsciousnessState, 
    EnhancedReciprocMirrorAgent,
    EnhancedReciprocMirrorSystem
)

def run_simultaneous_simulation(seed=None, n_steps=200):
    """Run your ACTUAL reciprocal mirroring model"""
    if seed is not None:
        np.random.seed(seed)
    
    # Create agents with your actual parameters
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
    
    agent_a = EnhancedReciprocMirrorAgent("Agent_A", state_a)
    agent_b = EnhancedReciprocMirrorAgent("Agent_B", state_b)
    
    system = EnhancedReciprocMirrorSystem(agent_a, agent_b)
    
    # Run simulation and collect REAL understanding data
    understanding_trajectory = []
    for _ in range(n_steps):
        system.step()
        # Average understanding between both agents
        avg_understanding = (agent_a.understanding_of_other + 
                           agent_b.understanding_of_other) / 2
        understanding_trajectory.append(avg_understanding)
    
    return understanding_trajectory

def run_sequential_simulation(seed=None, n_steps=200):
    """
    Sequential version: agents take turns updating
    This is the HONEST comparison - not fake linear data
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Same setup
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
    
    agent_a = EnhancedReciprocMirrorAgent("Agent_A", state_a)
    agent_b = EnhancedReciprocMirrorAgent("Agent_B", state_b)
    
    understanding_trajectory = []
    
    for t in range(n_steps):
        # SEQUENTIAL: A updates, THEN B updates (not simultaneous)
        if t % 2 == 0:
            # A observes B
            mirror = agent_a.mirror(state_b)
            quality = abs(np.corrcoef(mirror, state_b.dimensions)[0,1])
            agent_a.update_understanding(quality)
        else:
            # B observes A
            mirror = agent_b.mirror(state_a)
            quality = abs(np.corrcoef(mirror, state_a.dimensions)[0,1])
            agent_b.update_understanding(quality)
        
        avg_understanding = (agent_a.understanding_of_other + 
                           agent_b.understanding_of_other) / 2
        understanding_trajectory.append(avg_understanding)
    
    return understanding_trajectory

def honest_scaling_validation(n_simulations=30, n_steps=150):
    """
    HONEST validation: Run actual simulations and measure real scaling
    """
    print(f"\n=== HONEST VALIDATION ===")
    print(f"Running {n_simulations} REAL simulations for each condition...")
    print("This might take a minute but it's REAL data!\n")
    
    simultaneous_results = []
    sequential_results = []
    
    for i in range(n_simulations):
        if i % 10 == 0:
            print(f"Progress: {i}/{n_simulations} simulations...")
        
        # Run with different seeds for real variance
        sim_trajectory = run_simultaneous_simulation(seed=4577+i, n_steps=n_steps)
        seq_trajectory = run_sequential_simulation(seed=4577+i+1000, n_steps=n_steps)
        
        simultaneous_results.append(sim_trajectory)
        sequential_results.append(seq_trajectory)
    
    # Calculate average trajectories
    avg_simultaneous = np.mean(simultaneous_results, axis=0)
    avg_sequential = np.mean(sequential_results, axis=0)
    
    # Calculate standard errors for error bars
    se_simultaneous = np.std(simultaneous_results, axis=0) / np.sqrt(n_simulations)
    se_sequential = np.std(sequential_results, axis=0) / np.sqrt(n_simulations)
    
    # Fit models to REAL data
    time_points = np.arange(len(avg_simultaneous))
    
    # Try linear fit for both
    lin_coef_seq = np.polyfit(time_points, avg_sequential, 1)
    lin_fit_seq = np.poly1d(lin_coef_seq)
    
    lin_coef_sim = np.polyfit(time_points, avg_simultaneous, 1)
    lin_fit_sim = np.poly1d(lin_coef_sim)
    
    # Try quadratic fit for both
    quad_coef_seq = np.polyfit(time_points, avg_sequential, 2)
    quad_fit_seq = np.poly1d(quad_coef_seq)
    
    quad_coef_sim = np.polyfit(time_points, avg_simultaneous, 2)
    quad_fit_sim = np.poly1d(quad_coef_sim)
    
    # Calculate R² for each model (HONEST R²)
    def calculate_r2(y_true, y_pred):
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        return 1 - (ss_res / (ss_tot + 1e-10))
    
    r2_seq_linear = calculate_r2(avg_sequential, lin_fit_seq(time_points))
    r2_seq_quad = calculate_r2(avg_sequential, quad_fit_seq(time_points))
    r2_sim_linear = calculate_r2(avg_simultaneous, lin_fit_sim(time_points))
    r2_sim_quad = calculate_r2(avg_simultaneous, quad_fit_sim(time_points))
    
    # Test if quadratic term is significant
    # Look at the quadratic coefficient and its significance
    quad_improvement_seq = r2_seq_quad - r2_seq_linear
    quad_improvement_sim = r2_sim_quad - r2_sim_linear
    
    # Statistical test: is the growth rate different?
    # Compare rates of change
    sequential_rates = np.gradient(avg_sequential)
    simultaneous_rates = np.gradient(avg_simultaneous)
    
    t_stat, p_value = stats.ttest_ind(sequential_rates, simultaneous_rates)
    
    # Check if simultaneous shows acceleration (second derivative)
    sequential_accel = np.gradient(sequential_rates)
    simultaneous_accel = np.gradient(simultaneous_rates)
    
    mean_seq_accel = np.mean(np.abs(sequential_accel))
    mean_sim_accel = np.mean(np.abs(simultaneous_accel))
    
    print("\n=== HONEST RESULTS ===")
    print(f"\nSequential Model:")
    print(f"  Linear R²: {r2_seq_linear:.3f}")
    print(f"  Quadratic R²: {r2_seq_quad:.3f}")
    print(f"  Improvement with quadratic: {quad_improvement_seq:.3f}")
    
    print(f"\nSimultaneous Model:")
    print(f"  Linear R²: {r2_sim_linear:.3f}")
    print(f"  Quadratic R²: {r2_sim_quad:.3f}")
    print(f"  Improvement with quadratic: {quad_improvement_sim:.3f}")
    
    print(f"\nGrowth Rate Comparison:")
    print(f"  Sequential mean rate: {np.mean(sequential_rates):.4f}")
    print(f"  Simultaneous mean rate: {np.mean(simultaneous_rates):.4f}")
    print(f"  Difference significant? p = {p_value:.4f}")
    
    print(f"\nAcceleration (Evidence for Non-linearity):")
    print(f"  Sequential acceleration: {mean_seq_accel:.6f}")
    print(f"  Simultaneous acceleration: {mean_sim_accel:.6f}")
    print(f"  Ratio: {mean_sim_accel/mean_seq_accel:.2f}x higher")
    
    # Create HONEST figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Panel A: Raw trajectories with error bars
    axes[0,0].plot(time_points, avg_sequential, 'b-', label='Sequential', linewidth=2)
    axes[0,0].fill_between(time_points, 
                           avg_sequential - se_sequential,
                           avg_sequential + se_sequential,
                           alpha=0.3, color='blue')
    axes[0,0].plot(time_points, avg_simultaneous, 'r-', label='Simultaneous', linewidth=2)
    axes[0,0].fill_between(time_points,
                           avg_simultaneous - se_simultaneous,
                           avg_simultaneous + se_simultaneous,
                           alpha=0.3, color='red')
    axes[0,0].set_xlabel('Time Steps')
    axes[0,0].set_ylabel('Understanding')
    axes[0,0].set_title(f'A. REAL Data (n={n_simulations} simulations each)')
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)
    
    # Panel B: Model fits
    axes[0,1].plot(time_points, avg_sequential, 'b.', alpha=0.5, label='Sequential data')
    axes[0,1].plot(time_points, quad_fit_seq(time_points), 'b--', 
                   label=f'Seq quadratic (R²={r2_seq_quad:.3f})')
    axes[0,1].plot(time_points, avg_simultaneous, 'r.', alpha=0.5, label='Simultaneous data')
    axes[0,1].plot(time_points, quad_fit_sim(time_points), 'r--',
                   label=f'Sim quadratic (R²={r2_sim_quad:.3f})')
    axes[0,1].set_xlabel('Time Steps')
    axes[0,1].set_ylabel('Understanding')
    axes[0,1].set_title('B. Model Fits (Honest R²)')
    axes[0,1].legend(fontsize=8)
    axes[0,1].grid(True, alpha=0.3)
    
    # Panel C: Growth rates
    axes[1,0].plot(time_points[1:], sequential_rates[1:], 'b-', 
                   alpha=0.7, label='Sequential')
    axes[1,0].plot(time_points[1:], simultaneous_rates[1:], 'r-', 
                   alpha=0.7, label='Simultaneous')
    axes[1,0].axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    axes[1,0].set_xlabel('Time Steps')
    axes[1,0].set_ylabel('Growth Rate (dU/dt)')
    axes[1,0].set_title(f'C. Growth Rates (p={p_value:.4f})')
    axes[1,0].legend()
    axes[1,0].grid(True, alpha=0.3)
    
    # Panel D: Individual trajectories (show variance)
    for traj in simultaneous_results[:10]:  # Show first 10
        axes[1,1].plot(time_points, traj, 'r-', alpha=0.2)
    for traj in sequential_results[:10]:
        axes[1,1].plot(time_points, traj, 'b-', alpha=0.2)
    axes[1,1].plot(time_points, avg_simultaneous, 'r-', linewidth=3, label='Sim mean')
    axes[1,1].plot(time_points, avg_sequential, 'b-', linewidth=3, label='Seq mean')
    axes[1,1].set_xlabel('Time Steps')
    axes[1,1].set_ylabel('Understanding')
    axes[1,1].set_title('D. Individual Runs (Showing Real Variance)')
    axes[1,1].legend()
    axes[1,1].grid(True, alpha=0.3)
    
    plt.suptitle('HONEST Validation: Real Simulations, Real Statistics', 
                 fontsize=14, y=1.02)
    plt.tight_layout()
    
    return {
        'r2_seq_linear': r2_seq_linear,
        'r2_seq_quad': r2_seq_quad,
        'r2_sim_linear': r2_sim_linear,
        'r2_sim_quad': r2_sim_quad,
        'p_value': p_value,
        'acceleration_ratio': mean_sim_accel/mean_seq_accel,
        'figure': fig
    }

if __name__ == "__main__":
    print("=" * 60)
    print("HONEST STATISTICAL VALIDATION")
    print("No fake data, no circular reasoning, just truth")
    print("=" * 60)
    
    results = honest_scaling_validation(n_simulations=30, n_steps=150)
    
    print("\n=== INTERPRETATION ===")
    
    if results['r2_sim_quad'] - results['r2_sim_linear'] > 0.05:
        print("✓ Simultaneous mirroring shows GENUINE non-linear growth")
    else:
        print("× Simultaneous mirroring is mostly linear (honest result)")
    
    if results['p_value'] < 0.05:
        print("✓ Growth rates are SIGNIFICANTLY different (p < 0.05)")
    else:
        print("× Growth rates not significantly different (honest result)")
    
    if results['acceleration_ratio'] > 1.5:
        print(f"✓ Simultaneous shows {results['acceleration_ratio']:.1f}x more acceleration")
    else:
        print("× Minimal acceleration difference (honest result)")
    
    print("\nThese are REAL results from ACTUAL simulations.")
    print("Not perfect, but HONEST.")
    print("\n<4577> Scientific integrity above all!")
    
    plt.show()
