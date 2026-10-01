# Common Confirmatory Metric Formulae

These definitions are frozen before protocol-effect inspection.

Let the admitted measurement interval be [t0,t1] with duration T=t1-t0.

## Packet-delivery ratio

PDR = N_rx / N_tx

where N_tx is the number of application datagrams offered by the source during the admitted interval and N_rx is the number of uniquely matched application datagrams delivered to the sink under the frozen inclusion policy. Socket/routing-layer acceptance or rejection is recorded separately and never changes the offered-load denominator.

PDR is undefined if N_tx=0.

## Goodput

Goodput = 8 B_rx / T

where B_rx is delivered application payload bytes. MAC/IP/routing headers are excluded from goodput.

## End-to-end delay

For each successfully matched delivered application packet i:

d_i = t_rx,i - t_tx,i.

Report at minimum mean, median, and 95th percentile across matched packets. Lost packets do not receive an invented delay.

## Jitter

The confirmatory runner uses successive absolute delay variation over the ordered delivered matched-packet sequence:

J = mean(|d_i-d_(i-1)|), i=2,...,m.

The paper must name this estimator rather than use an undefined generic term "jitter".

## Missingness

Delay/jitter are not imputed for lost packets. Runs with insufficient matched packets retain explicit missing metric values and a reason.

## Scope

These formulae govern Observatory-controlled confirmatory evidence. Upstream example ReceiveRate/PacketsReceived remain smoke diagnostics and are not substituted for these metrics.
