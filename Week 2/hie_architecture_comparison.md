# Exercise 21: HIE Architecture Comparison

| Architecture | Data Storage Location | Query Pattern | Privacy Implications | Scalability | Real-World Examples |
|---|---|---|---|---|---|
| Centralized HIE | Data is copied into a central repository | Query central database | Easier auditing but higher central breach risk | Good for analytics, but central repository can become large | State/regional repositories, clinical data warehouses |
| Federated HIE | Data stays at source organizations | Query is routed to participating systems | Less central data exposure, but depends on source system controls | Scales organizationally, but query performance varies | Network-based exchange, Carequality-style query models |
| Hybrid HIE | Some data centralized, some queried from sources | Combination of repository and federated query | Balanced model; sensitive data may remain local | Often practical for large HIEs | Regional HIEs with MPI/RLS plus document repositories |