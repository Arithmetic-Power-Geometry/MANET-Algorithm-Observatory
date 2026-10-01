# Common Confirmatory Metric Formulae

Let the admitted measurement interval be [t0, t1] with duration T = t1 - t0.

## Packet-delivery ratio

PDR = N_rx / N_tx

where N_tx is the number of application datagrams offered by the source during the admitted interval and N_rx is the number of uniquely matched application datagrams delivered to the sink under the common inclusion policy. Socket or routing-layer acceptance does not change the offered-load denominator.

PDR is undefined when N_tx = 0.

## Goodput

Goodput = 8 B_rx / T

where B_rx is the delivered application payload in bytes. MAC, IP, and routing headers are excluded.

## End-to-end delay

For each successfully matched delivered application packet i:

d_i = t_rx,i - t_tx,i.

Lost packets are not assigned an artificial delay.

## Jitter

Successive absolute delay variation is

J = mean(|d_i - d_(i-1)|), i = 2,...,m.

## Missingness

Delay and jitter are not imputed for lost packets. Runs with insufficient matched packets retain explicit missing values and a reason.

## Scope

These definitions govern the Observatory-controlled confirmatory measurements reported in the repository. Engineering smoke outputs are not substituted for these common metrics.
