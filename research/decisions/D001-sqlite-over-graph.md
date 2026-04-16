# D001: SQLite Over Graph Databases
**Date:** 2026-04-16
**Status:** active
**Tags:** database, infrastructure, scale

## Context
The fact registry needs a database for approximately 700 documents, 11K facts, and 2K entities. The question was which storage engine best fits the data model (entities, claims, provenance links) at this scale. Evaluated Neo4j, TypeDB, TerminusDB, RDF triple stores (Jena, Blazegraph, Stardog), and SQLite.

## Options Considered
**(A) Graph database** (Neo4j, TypeDB, TerminusDB) -- Natural entity-relationship model. Native graph traversal. But every option requires a JVM or dedicated server process, a backup strategy, and ongoing operational overhead. At ~11K facts the query advantage over relational is negligible.

**(B) RDF triple stores** (Jena, Blazegraph, Stardog) -- Clean provenance model via named graphs. SPARQL is purpose-built for the query patterns. But the impedance mismatch at this scale is massive: setting up a triple store, learning SPARQL, and maintaining an RDF serialization layer for a dataset that fits in a single CSV is unjustifiable.

**(C) SQLite** -- Zero infrastructure. File-based. Ships with Python's standard library. No server process, no backup orchestration, no network configuration. The entire database is a single file that can be versioned, copied, or inspected with standard tooling.

## Decision
SQLite. At this scale, every graph database and triple store adds operational overhead for zero query benefit. The relationships in the fact registry are 2-hop traversals (entity -> claim -> article), not deep graph walking or recursive path queries. Self-joins in SQL handle these patterns in milliseconds. The entire dataset fits comfortably in memory.

## Consequences
- No SPARQL. No native graph traversal operators.
- All relationship queries are expressed as JOINs and self-joins.
- Schema must be carefully designed since SQLite lacks rich type enforcement (no enums, no foreign key enforcement by default, no CHECK constraints on complex types).
- The database file can be committed to version control, copied between machines, and inspected with any SQLite client.
- Migration to a heavier database later is straightforward since the schema is relational.

## References
- Section C of initial database research (graph DB and triple store evaluation)
- Neo4j, TypeDB, TerminusDB operational requirements analysis
- rdflib and triple store impedance mismatch assessment
