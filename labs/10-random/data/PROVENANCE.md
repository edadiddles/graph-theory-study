# Karate-club network provenance

This is a locally saved unweighted projection of Zachary's karate-club network
as encoded in NetworkX 3.4.2. NetworkX is not installed or required by this lab.

- Original study: Wayne W. Zachary, "An Information Flow Model for Conflict and
  Fission in Small Groups," *Journal of Anthropological Research* 33 (1977),
  452-473, as cited by the upstream implementation.
- Pinned source: [`karate_club_graph`, NetworkX 3.4.2](https://raw.githubusercontent.com/networkx/networkx/networkx-3.4.2/networkx/generators/social.py).
- Upstream project: [NetworkX](https://networkx.org/).
- Original source license: [BSD 3-clause notice](https://raw.githubusercontent.com/networkx/networkx/networkx-3.4.2/LICENSE.txt),
  retained locally as [NETWORKX_LICENSE.txt](NETWORKX_LICENSE.txt).
- Local file: [karate_club.json](karate_club.json).
- Local JSON SHA-256:
  `ace09747bb2d0bb7a43d11e1c7cada95cedd7f3b34699142a5686b6e4407e7dd`.

## Representation and transformation

The upstream function contains a 34-by-34 integer adjacency literal and adds an
undirected edge for each positive entry. The local extraction parsed that data
literal as numbers without executing the source or importing NetworkX. Each
unordered pair is retained if either directed matrix entry is positive, matching
undirected edge insertion. Only edge presence is retained; numerical interaction
weights are discarded. Do not assume that reading only one matrix triangle is
equivalent to the source's insertion procedure.

Upstream zero-based IDs 0 through 33 are converted to decimal strings without
changing identity. Every vertex is explicit. Each local edge is stored once,
with endpoints sorted lexically as strings; the edge list is sorted lexically
as well. The projection has 34 vertices and 78 distinct undirected edges.
Club-affiliation attributes and weights are omitted from this lab's file.

The source is a processed representation of an observational social network,
not a new measurement or a record-linkage dataset. Vertices represent club
members and edges represent ties in that source representation. Do not interpret
adjacency as shared identity, or use this projection to make claims about weights
or labels that it does not retain. No summary answer, ensemble comparison, or
model-adequacy conclusion is supplied here.

The JSON includes source metadata for reproducibility. The checksum validates
this saved snapshot; it is not a claim about the bytes of the upstream source.
All normal lab work and tests are offline. Keep this provenance and license
notice with copies of the derived data.
