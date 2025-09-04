# Hassling with war - Predictability
import numpy as np
import matplotlib.pyplot as plt


N = 200

##### Setting Up Constants #####
# f(alpha, theta)
f_ll = 0.5
f_lh = 1
f_hl = 0.8
f_hh = 1.1

# war payoff for a and d
omega_a = 0.4
omega_d = 0.1
p = 0.5

# Type probabilities, Pr(low_theta) or Pr(high_theta)
pr_l = 0.5
pr_h = 1 - pr_l

# selected h's across types h_alphatheta
h_ll = f_ll / 2
h_lh = f_lh / 2
h_hl = f_hl / 2
h_hh = f_hh / 2

# cutpoints for D to go to war. t_cut_alphatheta
t_cut_ll = omega_a + omega_d + f_ll / 4
t_cut_lh = omega_a + omega_d + f_lh / 4
t_cut_hl = omega_a + omega_d + f_hl / 4
t_cut_hh = omega_a + omega_d + f_hh / 4

# theta high and low, calculate theta_til high and low
t_low = 0.575
t_high = 0.825
t_span = np.linspace(t_low, t_high, N)

# Intermediate values; for processing. These are if selected t never led to
# war, sometimes led to war, always led to war. Use cutpoints in forloop
# below to correct
InterEU_A_no_war_al = (p - omega_a) * np.ones(N) + t_span + pr_l * np.ones(N) * (-h_ll) + pr_h * np.ones(N) * (-h_lh)
InterEU_A_some_war_al = pr_l * np.ones(N) * (p - omega_a) + pr_h * ((p - h_lh - omega_a) * np.ones(N) + t_span)
InterEU_A_all_war_al = np.ones(N) * (p - omega_a)

InterEU_A_no_war_ah = (p - omega_a) * np.ones(N) + t_span + pr_l * np.ones(N) * (-h_hl) + pr_h * np.ones(N) * (-h_hh)
InterEU_A_some_war_ah = pr_l * np.ones(N) * (p - omega_a) + pr_h * ((p - h_hh - omega_a) * np.ones(N) + t_span)
InterEU_A_all_war_ah = np.ones(N) * (p - omega_a)

EU_A_al = np.zeros(N)
for i in range(N):
    if t_span[i] < t_cut_ll:
        EU_A_al[i] = InterEU_A_no_war_al[i]
    elif t_span[i] > t_cut_lh:
        EU_A_al[i] = InterEU_A_all_war_al[i]
    else:
        EU_A_al[i] = InterEU_A_some_war_al[i]

EU_A_ah = np.zeros(N)
for i in range(N):
    if t_span[i] < t_cut_hl:
        EU_A_ah[i] = InterEU_A_no_war_ah[i]
    elif t_span[i] > t_cut_hh:
        EU_A_ah[i] = InterEU_A_all_war_ah[i]
    else:
        EU_A_ah[i] = InterEU_A_some_war_ah[i]

# Print some results (replacing the 'qqq' debug line)
print("Predictability script completed successfully!")
print(f"EU_A_al shape: {EU_A_al.shape}")
print(f"EU_A_ah shape: {EU_A_ah.shape}")
print(f"First 5 values of EU_A_al: {EU_A_al[:5]}")
print(f"First 5 values of EU_A_ah: {EU_A_ah[:5]}")

# Create stacked subplots like the attached figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Top subplot - EU_A_al (α = low)
ax1.plot(t_span, EU_A_al, 'b-', linewidth=2, marker='o', markersize=4)
ax1.set_ylabel('EU_A', fontsize=12)
ax1.set_title("C's Utility Across θ_N for α_l (Predictability)", fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_ylim([min(EU_A_al) - 0.02, max(EU_A_al) + 0.02])

# Add cutpoint markers
ax1.axvline(x=t_cut_ll, color='red', linestyle='--', alpha=0.7, label=f't_cut_ll = {t_cut_ll:.3f}')
ax1.axvline(x=t_cut_lh, color='orange', linestyle='--', alpha=0.7, label=f't_cut_lh = {t_cut_lh:.3f}')
ax1.legend(fontsize=10)

# Bottom subplot - EU_A_ah (α = high)
ax2.plot(t_span, EU_A_ah, 'g-', linewidth=2, marker='s', markersize=4)
ax2.set_xlabel('t_span', fontsize=12)
ax2.set_ylabel('EU_A', fontsize=12)
ax2.set_title("C's Utility Across θ_N for α_h (Predictability)", fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.set_ylim([min(EU_A_ah) - 0.02, max(EU_A_ah) + 0.02])

# Add cutpoint markers
ax2.axvline(x=t_cut_hl, color='red', linestyle='--', alpha=0.7, label=f't_cut_hl = {t_cut_hl:.3f}')
ax2.axvline(x=t_cut_hh, color='orange', linestyle='--', alpha=0.7, label=f't_cut_hh = {t_cut_hh:.3f}')
ax2.legend(fontsize=10)

plt.tight_layout()
plt.show()
