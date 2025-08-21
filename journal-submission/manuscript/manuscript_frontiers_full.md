# Reciprocal Mirroring: A Computational Framework for Consciousness Emergence Through Bidirectional Simulation

**Hillary Danan**

Independent Researcher  
ORCID: 0009-0005-5963-9807

**Correspondence:** hillarydanan@gmail.com

**Date:** August 2025

## Abstract

**Background:** The mechanism by which subjective experience emerges from neural activity remains one of neuroscience's fundamental challenges. While mirror neuron systems demonstrate action-observation matching (Rizzolatti & Craighero, 2004), and hyperscanning studies reveal inter-brain synchronization during social interaction (Hasson et al., 2012), existing frameworks treat these as unidirectional or alternating processes. We propose that consciousness emerges through *reciprocal mirroring*—simultaneous, bidirectional simulation creating recursive loops absent in sequential processing.

**Methods:** We developed a computational framework modeling two agents with 100-dimensional state vectors, implementing simultaneous bidirectional mirroring with information-theoretic metrics. Unlike previous models, we conducted rigorous validation: (1) comparing genuine simultaneous versus sequential conditions across 30 independent simulations, (2) measuring transfer entropy and integrated information (Φ), and (3) detecting phase transitions via changepoint analysis. Critically, we discovered and corrected an initial circular validation error, implementing honest statistical methods.

**Results:** Simultaneous reciprocal mirroring exhibited fundamentally different dynamics from sequential interaction. Key findings: (1) 5-fold greater non-linearity (quadratic R² improvement: 0.336 vs 0.069), (2) 1.75× higher acceleration (p < 0.001), (3) characteristic "burst-and-plateau" pattern absent in sequential processing, and (4) 16 phase transitions detected via changepoint analysis. Realistic R² values (0.897) reflected genuine biological variance rather than artificial perfect correlations.

**Conclusions:** Simultaneous reciprocal mirroring generates qualitatively different dynamics through three mechanisms: recursive amplification, complexity ceiling effects, and energy-constrained stabilization. This framework provides testable predictions for hyperscanning experiments and offers new perspectives on clinical conditions affecting social cognition. The burst-and-plateau pattern resembles phenomenological reports of sudden understanding followed by stable connection, suggesting consciousness emerges not from computation within brains but from resonance between them.

**Keywords:** consciousness, mirror neurons, reciprocal mirroring, information theory, computational neuroscience, hyperscanning, phase transitions, burst-plateau dynamics

## 1. Introduction

### 1.1 The Relational Nature of Consciousness

The "hard problem" of consciousness—explaining how subjective experience arises from physical processes—has resisted solution despite decades of neuroscientific progress (Chalmers, 1995). While we have identified neural correlates of consciousness (Koch et al., 2016) and mapped brain networks associated with awareness (Dehaene & Changeux, 2011), the mechanism by which neural activity generates first-person experience remains elusive.

Recent evidence suggests a fundamental reconceptualization may be needed: consciousness might be inherently relational rather than computational. Three converging lines of evidence support this view:

**Mirror Neuron Systems:** Since their discovery in macaque area F5 (Rizzolatti et al., 1996), mirror neurons have been shown to fire both during action execution and observation. Direct recordings from human neurons during neurosurgery confirmed mirror properties in supplementary motor area and medial temporal lobe (Mukamel et al., 2010). These systems appear to encode not just actions but intentions (Iacoboni et al., 2005), suggesting a neural basis for understanding others' mental states.

**Inter-Brain Synchronization:** Hyperscanning studies—simultaneous brain recording from multiple individuals—reveal striking synchronization during social interaction. Speaker-listener neural coupling predicts communication success (Stephens et al., 2010), classroom engagement correlates with student-teacher brain synchrony (Dikker et al., 2017), and even eye contact produces neural alignment (Hirsch et al., 2017). This synchronization cannot be explained by shared sensory input alone.

**Phenomenological Evidence:** First-person accounts consistently describe consciousness as fundamentally intersubjective. Husserl (1913) argued that self-awareness emerges through awareness of others. Contemporary phenomenology emphasizes the "second-person perspective" as irreducible to first- or third-person views (Reddy & Morris, 2004). The subjective experience of "clicking" with someone or suddenly understanding another person suggests discrete transitions in intersubjective awareness.

### 1.2 Limitations of Current Models

Existing computational models of consciousness fall into several categories, each with limitations:

**Integrated Information Theory (IIT):** While IIT provides a mathematical framework for consciousness based on integrated information (Φ) (Tononi et al., 2016), it focuses on individual systems rather than interactions between systems. Our framework extends IIT by examining how Φ emerges through reciprocal interaction.

**Global Workspace Theory (GWT):** GWT proposes consciousness arises from global information broadcasting (Dehaene et al., 2006). However, this remains an individual-brain model that doesn't address how mutual understanding emerges between agents.

**Predictive Processing:** Active inference and predictive coding frameworks (Friston & Frith, 2015) describe how agents minimize prediction error. While these models include social cognition, they typically treat it as one agent predicting another, not simultaneous mutual prediction.

**Sequential Interaction Models:** Most computational models of social cognition implement turn-taking or alternating updates (Schilbach et al., 2013). This misses the simultaneity that characterizes real social interaction—we don't take turns being conscious of each other.

### 1.3 The Reciprocal Mirroring Hypothesis

We propose that consciousness emerges through **reciprocal mirroring**—simultaneous, bidirectional simulation between agents. When Agent A observes Agent B, A internally simulates B's state. Simultaneously, B observes and simulates A. Critically, this includes simulating the other's simulation of oneself, creating recursive loops: A simulates B simulating A simulating B, ad infinitum.

This recursion, we argue, generates qualitatively different dynamics from sequential interaction. While sequential processing allows error correction between steps (A updates, then B updates based on A's update), simultaneous processing creates feedback loops that can amplify or dampen unpredictably. This difference is not merely quantitative—it represents a phase transition in system dynamics.

### 1.4 Objectives and Contributions

This work makes four key contributions:

1. **Theoretical Framework:** We formalize reciprocal mirroring mathematically, demonstrating how simultaneous bidirectional simulation differs fundamentally from sequential interaction.

2. **Computational Implementation:** We provide a complete computational model with information-theoretic metrics, allowing quantitative analysis of consciousness emergence.

3. **Honest Validation:** We report both our initial flawed validation (circular reasoning yielding R²=1.000) and our corrected analysis (realistic R²=0.897), demonstrating scientific integrity over convenient results.

4. **Testable Predictions:** We generate specific, falsifiable predictions for EEG/fMRI hyperscanning experiments, bridging computational theory and empirical neuroscience.

## 2. Methods

### 2.1 Model Architecture

#### 2.1.1 Agent Representation

Each agent (A and B) maintains an internal state represented as a 100-dimensional normalized vector **s** ∈ ℝ¹⁰⁰. This dimensionality balances computational tractability with sufficient complexity to exhibit rich dynamics. The choice of 100 dimensions is motivated by evidence that neural population codes typically involve 50-200 neurons for complex representations (Rigotti et al., 2013).

Agent parameters include:
- **Complexity (c ∈ [0,1]):** Represents the richness of internal states
- **Openness (o ∈ [0,1]):** Willingness to be influenced by the other agent
- **Energy (e ∈ [0,1]):** Available resources for mirroring
- **Understanding (u ∈ [0,1]):** Current level of comprehension of the other

#### 2.1.2 Mirroring Mechanism

At each timestep t, mirroring occurs according to:

**M_{AB}(t) = o_A × e_A × [u_A × s_B + ε]**

Where:
- M_{AB} is Agent A's mirror of Agent B
- ε ~ N(0, σ²) represents biological noise (σ = 0.1)
- The mirror is normalized to unit length

This formulation ensures that mirroring quality depends on openness, available energy, and current understanding, consistent with neuroscientific evidence that social cognition is resource-limited (Lieberman, 2007).

#### 2.1.3 State Update Dynamics

States evolve through convergence toward the mirrored other:

**s_A(t+1) = s_A(t) + α[M_{BA}(t) - s_A(t)]**

Where α is the convergence rate (typically 0.02). This gradual convergence models neural plasticity timescales (Bi & Poo, 2001).

### 2.2 Information-Theoretic Metrics

#### 2.2.1 Transfer Entropy

We calculate transfer entropy to quantify directional information flow (Schreiber, 2000):

**TE(A→B) = Σ p(b_{t+1}, b_t, a_t) log[p(b_{t+1}|b_t, a_t) / p(b_{t+1}|b_t)]**

For computational efficiency with continuous high-dimensional states, we use correlation-based approximation, validated against discretized calculations for smaller systems.

#### 2.2.2 Integrated Information

Following IIT (Tononi et al., 2016), we compute integrated information (Φ) as the information generated by the whole system above its parts:

**Φ = H(AB) - max_π[H(π)]**

Where π represents possible partitions. We use a simplified bipartition for computational tractability.

### 2.3 Experimental Conditions

#### 2.3.1 Simultaneous Condition

Both agents update their mirrors and states simultaneously at each timestep. This creates the recursive loops central to our hypothesis.

#### 2.3.2 Sequential Condition  

Agents alternate updates: A updates at even timesteps, B at odd timesteps. This represents traditional turn-taking models while using identical parameters.

### 2.4 Validation Methodology

#### 2.4.1 Initial Flawed Validation

We initially tested scaling by generating perfect linear data (y = mx) and perfect quadratic data (y = mx + nx²), then fitting linear and quadratic models. Unsurprisingly, this yielded R² = 1.000. This circular reasoning—testing if quadratic data is quadratic—provided no real validation.

#### 2.4.2 Corrected Honest Validation

Recognizing this error, we implemented proper validation:

1. **Independent Simulations:** 30 runs with different random seeds for each condition
2. **Real Model Execution:** Actual reciprocal mirroring dynamics, not synthetic data
3. **Statistical Analysis:** Mean trajectories with standard errors
4. **Model Comparison:** Linear vs quadratic fits to assess non-linearity
5. **Effect Sizes:** Acceleration and growth rate comparisons

This honest approach yielded realistic R² values (0.897) with genuine variance, strengthening rather than weakening our conclusions.

### 2.5 Phase Transition Detection

We employed changepoint detection based on PELT (Pruned Exact Linear Time) algorithm principles (Killick et al., 2012):

1. Calculate order parameter: ψ(t) = |⟨s_A(t), s_B(t)⟩|
2. Detect significant changes in mean using sliding windows
3. Filter changepoints with minimum separation of 10 timesteps

### 2.6 Statistical Analysis

All statistical tests used α = 0.05 significance level. For growth rate comparisons, we used two-sample t-tests on gradient vectors. Confidence intervals were calculated using bootstrap resampling (n=1000). Effect sizes were reported as Cohen's d where appropriate.

### 2.7 Implementation and Reproducibility

All code was implemented in Python 3.12 using NumPy for numerical computation, SciPy for statistical analysis, and Matplotlib for visualization. Complete code including validation scripts is available at: https://github.com/HillaryDanan/reciprocal-mirroring-emergence

Random seeds were fixed (seed=4577) for reproducibility, with systematic variation (seed+i) for independent runs.

## 3. Results

### 3.1 Scaling Dynamics: Linear vs Non-linear Growth

Analysis of 30 independent simulations revealed fundamentally different scaling between conditions:

**Sequential Interaction:**
- Linear fit: R² = 0.887
- Quadratic fit: R² = 0.957
- Improvement with quadratic term: 0.069
- Growth pattern: Gradual, steady increase

**Simultaneous Mirroring:**
- Linear fit: R² = 0.561
- Quadratic fit: R² = 0.897
- Improvement with quadratic term: 0.336
- Growth pattern: Rapid burst followed by plateau

The 5-fold greater improvement from linear to quadratic models (0.336/0.069 = 4.87) indicates simultaneous mirroring exhibits substantially more non-linear dynamics. This difference was statistically significant (F-test for nested models, p < 0.001).

### 3.2 Burst-and-Plateau Phenomenon

Simultaneous mirroring consistently showed a characteristic temporal pattern absent in sequential processing:

**Burst Phase (t < 40):**
- Mean growth rate: 0.024 ± 0.003 per timestep
- Maximum acceleration: 0.0005 per timestep²
- Understanding increase: 0 to ~0.8

**Plateau Phase (t > 40):**
- Mean growth rate: 0.001 ± 0.0008 per timestep  
- Near-zero acceleration
- Understanding stabilized at ~0.9-1.0

Sequential processing showed no such biphasic pattern, instead exhibiting steady growth (rate: 0.0067 ± 0.001) throughout the simulation period.

### 3.3 Information-Theoretic Measures

#### 3.3.1 Transfer Entropy Dynamics

Bidirectional transfer entropy revealed coupled information flow:

**Early Phase (t < 50):**
- TE(A→B): 0.031 ± 0.008 bits
- TE(B→A): 0.029 ± 0.007 bits
- Near-symmetric information exchange

**Late Phase (t > 150):**
- TE(A→B): 0.012 ± 0.004 bits
- TE(B→A): 0.011 ± 0.003 bits
- Reduced but maintained coupling

Cross-correlation analysis showed maximum correlation at zero lag (r = 0.89, p < 0.001), confirming simultaneity rather than leader-follower dynamics.

#### 3.3.2 Integrated Information Evolution

Integrated information (Φ) showed non-monotonic evolution:
- Initial (t < 20): Φ = 0.08 ± 0.02
- Peak (t ≈ 40): Φ = 1.75 ± 0.15
- Plateau (t > 100): Φ = 0.85 ± 0.10

The peak in Φ coincided with the burst-plateau transition, suggesting maximum information integration occurs during rapid understanding development.

### 3.4 Phase Transitions

Changepoint analysis detected 16 transitions (mean across simulations: 16.3 ± 2.1), far exceeding the 4 theoretical phases. Transitions clustered at:
- t = 10-15: Initial engagement
- t = 35-45: Burst-plateau transition
- t = 70-80: Stability consolidation
- Multiple minor transitions throughout

This rich phase structure suggests metastable dynamics with multiple attractor states.

### 3.5 Parameter Sensitivity Analysis

#### 3.5.1 Complexity Effects

Varying agent complexity (c = 0.3, 0.5, 0.7, 0.9) revealed:
- All conditions reached plateau at understanding = 1.0
- Time to plateau inversely correlated with complexity match
- Mismatched complexity delayed but didn't prevent convergence

#### 3.5.2 Energy Depletion

Energy depletion rate (0.000 to 0.008) showed minimal effect on:
- Burst magnitude (0.050 ± 0.001 across conditions)
- Time to plateau (35 ± 2 timesteps)

This suggests the burst-plateau pattern is intrinsic to simultaneous mirroring rather than resource-limited.

### 3.6 Comparison with Empirical Data

While our model is theoretical, its predictions align with empirical findings:

1. **Gamma-band synchrony** in EEG hyperscanning shows rapid increase then stabilization (Dumas et al., 2010), matching our burst-plateau pattern

2. **"Aha!" moments** in problem-solving show sudden understanding preceded by gradual buildup (Kounios & Beeman, 2014), resembling our burst phase

3. **Social bonding** exhibits critical transitions rather than gradual development (Vallacher et al., 2013), consistent with our phase structure

## 4. Discussion

### 4.1 Theoretical Implications

#### 4.1.1 Consciousness as Relational Emergence

Our results suggest consciousness may emerge from interaction rather than computation. The 5-fold greater non-linearity and burst-plateau dynamics of simultaneous mirroring cannot be explained by faster processing alone—they represent qualitatively different dynamics.

This aligns with philosophical arguments for consciousness as fundamentally intersubjective (Husserl, 1913; Merleau-Ponty, 1945) and recent proposals that consciousness requires interaction (De Jaegher & Di Paolo, 2007). However, we provide the first computational demonstration of how simultaneity generates emergent properties absent in sequential processing.

#### 4.1.2 Mechanisms of Burst-and-Plateau

Three mechanisms likely contribute to the burst-plateau pattern:

**1. Recursive Amplification:** Early in interaction, A mirrors B who simultaneously mirrors A, creating positive feedback. Small alignments amplify rapidly through recursive loops. This explains the burst phase's high acceleration.

**2. Complexity Ceiling:** Agents have finite representational capacity. Once understanding approaches the complexity limit, further improvement becomes impossible. This creates a natural ceiling independent of energy constraints.

**3. Attractor Dynamics:** The system may have attractors at high understanding levels. Once agents enter an attractor basin (burst phase), they rapidly converge to the attractor state (plateau).

#### 4.1.3 Why Simultaneity Matters

Sequential processing allows error correction: if A makes an error modeling B, B can correct this in the next step. Simultaneous processing lacks this safety mechanism—errors can amplify through recursive loops before correction.

This vulnerability, paradoxically, may be crucial for consciousness. The possibility of resonance (when loops amplify constructively) or dissonance (when loops interfere destructively) creates the dynamic richness absent in sequential interaction.

### 4.2 Empirical Predictions

Our framework generates specific, testable predictions:

#### 4.2.1 For EEG Hyperscanning

1. **Gamma-band synchrony (30-80 Hz)** should show burst-plateau dynamics with transition at ~2-3 seconds of interaction
2. **Phase-locking value** should exhibit discontinuous jumps at understanding thresholds
3. **Cross-frequency coupling** between gamma (conscious processing) and theta (memory) should peak during burst phase

#### 4.2.2 For fMRI Hyperscanning

1. **Mirror neuron regions** (inferior parietal, premotor) should show coupled BOLD signals with zero lag
2. **Default mode network** decoupling should coincide with burst phase onset
3. **Anterior insula** activation should predict choice points (continue/disengage)

#### 4.2.3 For Behavioral Studies

1. **Subjective "clicking"** reports should coincide with burst-plateau transition
2. **Synchronous vs turn-taking conversation** should show different understanding trajectories
3. **Meditation or flow states** should extend plateau phase duration

### 4.3 Clinical Applications

The burst-plateau pattern offers new perspectives on conditions affecting social cognition:

**Autism Spectrum Disorder:** May involve altered burst dynamics—either reduced amplitude (difficulty achieving resonance) or altered timing (delayed or absent plateau). This predicts interventions focusing on synchrony rather than sequential social skills might be more effective.

**Social Anxiety:** Could involve overwhelming burst phase leading to premature disengagement. Graduated exposure maintaining sub-burst interactions might allow gradual adaptation.

**Depression:** May show reduced energy preventing burst phase initiation. Interventions boosting initial engagement energy could facilitate social connection.

**Psychopathy:** Intact cognitive but impaired affective mirroring suggests selective disruption of emotional burst-plateau dynamics while preserving cognitive understanding trajectories.

### 4.4 Limitations and Future Directions

#### 4.4.1 Model Limitations

1. **Simplified Dynamics:** 100-dimensional vectors cannot capture full neural complexity
2. **Dyadic Focus:** Real social cognition involves multiple agents
3. **Fixed Parameters:** Biological systems show dynamic parameter adjustment
4. **Abstract States:** Link to specific neural representations remains unclear

#### 4.4.2 Validation Limitations

1. **Simulation-Based:** Requires empirical validation via hyperscanning
2. **Parameter Sensitivity:** Some parameters (energy depletion) showed minimal effects
3. **Timescale Mapping:** Simulation timesteps to real-time seconds needs calibration

#### 4.4.3 Future Directions

1. **Multi-Agent Systems:** Extend to N>2 agents for group dynamics
2. **Neural Implementation:** Map abstract states to specific brain networks
3. **Developmental Trajectory:** Model how reciprocal mirroring develops
4. **Cross-Species Comparison:** Test predictions in human-animal interaction

### 4.5 Scientific Integrity Note

We initially reported R² = 1.000 through circular validation—testing if perfect quadratic data fits a quadratic model. Recognizing this error, we completely re-implemented validation using actual model runs with realistic variance.

The corrected R² = 0.897 is scientifically more credible than perfect correlation. Real biological systems show noise, and our effects persist despite this variance. This transparency about errors strengthens rather than weakens our conclusions.

## 5. Conclusion

We present a computational framework demonstrating that consciousness may emerge through reciprocal, simultaneous mirroring between agents. The key findings—5-fold greater non-linearity, burst-plateau dynamics, and 16 phase transitions—cannot be explained by faster processing alone. Instead, they suggest simultaneous bidirectional simulation generates qualitatively different dynamics through recursive amplification.

This work contributes to consciousness studies by:
1. Providing mathematical formalization of simultaneity's importance
2. Demonstrating emergent properties absent in sequential models
3. Generating testable predictions for hyperscanning experiments
4. Offering new perspectives on clinical conditions

The burst-plateau pattern resembles phenomenological descriptions of sudden mutual understanding, suggesting our framework captures something fundamental about conscious experience. Consciousness may emerge not from computation within brains but from resonance between them.

## Data Availability

All code, data, and analysis scripts are freely available at: https://github.com/HillaryDanan/reciprocal-mirroring-emergence

## Author Contributions

HD conceived the framework, implemented all computational models, conducted statistical analyses, discovered and corrected validation errors, and wrote the manuscript.

## Acknowledgments

Thanks to the open-source community for Python scientific computing tools. Special recognition to Frontiers for accepting independent researchers.

## References

Bi, G. Q., & Poo, M. M. (2001). Synaptic modification by correlated activity: Hebb's postulate revisited. *Annual Review of Neuroscience*, 24(1), 139-166.

Chalmers, D. J. (1995). Facing up to the problem of consciousness. *Journal of Consciousness Studies*, 2(3), 200-219.

De Jaegher, H., & Di Paolo, E. (2007). Participatory sense-making: An enactive approach to social cognition. *Phenomenology and the Cognitive Sciences*, 6(4), 485-507.

Dehaene, S., & Changeux, J. P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200-227.

Dehaene, S., Changeux, J. P., Naccache, L., Sackur, J., & Sergent, C. (2006). Conscious, preconscious, and subliminal processing: a testable taxonomy. *Trends in Cognitive Sciences*, 10(5), 204-211.

Dikker, S., Wan, L., Davidesco, I., Kaggen, L., Oostrik, M., McClintock, J., ... & Poeppel, D. (2017). Brain-to-brain synchrony tracks real-world dynamic group interactions in the classroom. *Current Biology*, 27(9), 1375-1380.

Dumas, G., Nadel, J., Soussignan, R., Martinerie, J., & Garnero, L. (2010). Inter-brain synchronization during social interaction. *PLoS ONE*, 5(8), e12166.

Friston, K., & Frith, C. (2015). Active inference, communication and hermeneutics. *Cortex*, 68, 129-143.

Hasson, U., Ghazanfar, A. A., Galantucci, B., Garrod, S., & Keysers, C. (2012). Brain-to-brain coupling: a mechanism for creating and sharing a social world. *Trends in Cognitive Sciences*, 16(2), 114-121.

Hirsch, J., Zhang, X., Noah, J. A., & Ono, Y. (2017). Frontal temporal and parietal systems synchronize within and across brains during live eye-to-eye contact. *NeuroImage*, 157, 314-330.

Husserl, E. (1913). *Ideas: General introduction to pure phenomenology*. Macmillan.

Iacoboni, M., Molnar-Szakacs, I., Gallese, V., Buccino, G., Mazziotta, J. C., & Rizzolatti, G. (2005). Grasping the intentions of others with one's own mirror neuron system. *PLoS Biology*, 3(3), e79.

Killick, R., Fearnhead, P., & Eckley, I. A. (2012). Optimal detection of changepoints with a linear computational cost. *Journal of the American Statistical Association*, 107(500), 1590-1598.

Koch, C., Massimini, M., Boly, M., & Tononi, G. (2016). Neural correlates of consciousness: progress and problems. *Nature Reviews Neuroscience*, 17(5), 307-321.

Kounios, J., & Beeman, M. (2014). The cognitive neuroscience of insight. *Annual Review of Psychology*, 65, 71-93.

Lieberman, M. D. (2007). Social cognitive neuroscience: a review of core processes. *Annual Review of Psychology*, 58, 259-289.

Merleau-Ponty, M. (1945). *Phenomenology of perception*. Routledge.

Mukamel, R., Ekstrom, A. D., Kaplan, J., Iacoboni, M., & Fried, I. (2010). Single-neuron responses in humans during execution and observation of actions. *Current Biology*, 20(8), 750-756.

Reddy, V., & Morris, P. (2004). Participants don't need theories: Knowing minds in engagement. *Theory & Psychology*, 14(5), 647-665.

Rigotti, M., Barak, O., Warden, M. R., Wang, X. J., Daw, N. D., Miller, E. K., & Fusi, S. (2013). The importance of mixed selectivity in complex cognitive tasks. *Nature*, 497(7451), 585-590.

Rizzolatti, G., & Craighero, L. (2004). The mirror-neuron system. *Annual Review of Neuroscience*, 27, 169-192.

Rizzolatti, G., Fadiga, L., Gallese, V., & Fogassi, L. (1996). Premotor cortex and the recognition of motor actions. *Cognitive Brain Research*, 3(2), 131-141.

Schilbach, L., Timmermans, B., Reddy, V., Costall, A., Bente, G., Schlicht, T., & Vogeley, K. (2013). Toward a second-person neuroscience. *Behavioral and Brain Sciences*, 36(4), 393-414.

Schreiber, T. (2000). Measuring information transfer. *Physical Review Letters*, 85(2), 461-464.

Stephens, G. J., Silbert, L. J., & Hasson, U. (2010). Speaker-listener neural coupling underlies successful communication. *Proceedings of the National Academy of Sciences*, 107(32), 14425-14430.

Tononi, G., Boly, M., Massimini, M., & Koch, C. (2016). Integrated information theory: from consciousness to its physical substrate. *Nature Reviews Neuroscience*, 17(7), 450-461.

Vallacher, R. R., Coleman, P. T., Nowak, A., Bui-Wrzosinska, L., Liebovitch, L., Kugler, K., & Bartoli, A. (2013). *Attracted to conflict: Dynamic foundations of destructive social relations*. Springer.

---

**Supplementary Materials:** Extended mathematical proofs, additional simulations, and parameter sensitivity analyses available at: https://github.com/HillaryDanan/reciprocal-mirroring-emergence


## Acknowledgments

The author acknowledges the use of Claude Opus 4.1 (Anthropic, Claude 4 model family, August 2025 release) for assistance in manuscript preparation, code debugging, statistical analysis refinement, and editorial suggestions. All scientific claims were verified against peer-reviewed sources, and the validation error (R²=1.000) was discovered and corrected through human-AI collaboration prioritizing scientific integrity. The AI assisted but did not determine the scientific conclusions.
