%Hassling with war
clear all


N=200;

%%%%%Setting Up Constants%%%%%
%f(\alpha,\theta)
f_ll=0.5;
f_lh=1;
f_hl=0.8;
f_hh=1.1;

%war payoff for a and d
omega_a=0.4;
omega_d=0.1;
p=0.5;

%Type probabilities, Pr(low_theta) or Pr(high_theta)
pr_l=0.5;
pr_h=1-pr_l;

%selected h's across types h_alphatheta
h_ll=f_ll/2;
h_lh=f_lh/2;
h_hl=f_hl/2;
h_hh=f_hh/2;

%cutpoints for D to go to war. t_cut_alphatheta
t_cut_ll=omega_a + omega_d + f_ll/4;
t_cut_lh=omega_a + omega_d + f_lh/4;
t_cut_hl=omega_a + omega_d + f_hl/4;
t_cut_hh=omega_a + omega_d + f_hh/4;

%theta high and low, calculate theta_til high and low
t_low=0.575;
t_high=0.825;
t_span=linspace(t_low,t_high,N)';

%Intermediate values; for processing. These are if selected t never led to
%war, sometimes led to war, always led to war. Use cutpoints in forloop
%below to correct
InterEU_A_no_war_al=(p-omega_a)*ones(N,1)+t_span +  pr_l*ones(N,1)*(-h_ll)+ pr_h*ones(N,1)*(-h_lh);
InterEU_A_some_war_al=pr_l*ones(N,1)*(p-omega_a)+pr_h*((p-h_lh-omega_a)*ones(N,1)+t_span);
InterEU_A_all_war_al=ones(N,1)*(p-omega_a);

InterEU_A_no_war_ah=(p-omega_a)*ones(N,1)+t_span +  pr_l*ones(N,1)*(-h_hl)+ pr_h*ones(N,1)*(-h_hh);
InterEU_A_some_war_ah=pr_l*ones(N,1)*(p-omega_a)+pr_h*((p-h_hh-omega_a)*ones(N,1)+t_span);
InterEU_A_all_war_ah=ones(N,1)*(p-omega_a);

EU_A_al=zeros(N,1);
for i=1:N;
    if t_span(i)<t_cut_ll;
        EU_A_al(i)=InterEU_A_no_war_al(i);
    elseif t_span(i)>t_cut_lh;
        EU_A_al(i)=InterEU_A_all_war_al(i);
    else;
        EU_A_al(i)=InterEU_A_some_war_al(i);
    end;
end;




EU_A_ah=zeros(N,1);
for i=1:N;
    if t_span(i)<t_cut_hl;
        EU_A_ah(i)=InterEU_A_no_war_ah(i);
    elseif t_span(i)>t_cut_hh;
        EU_A_ah(i)=InterEU_A_all_war_ah(i);
    else;
        EU_A_ah(i)=InterEU_A_some_war_ah(i);
    end;
end;


qqq





