NOTE
====

This exercise is modified from a similar exercise created by Doug Palmer (doug.palmer@csiro.au).

Background
==========

The data management teams at ARGA and the ALA spends a lot of time analysing and translating
supplied data into a standardised form called Darwin Core (DwC, see below).
We usually get regular data updates from our sources, so we generally try to ensure
that any ETL tasks are repeatable.

We are in the process of persuading our data providers to send data as native Darwin Core.
This is still very much a work in progress and will require a lot of consulting work.

Task
====

Take the sample dataset and translate them into Darwin Core form.
We are not that much interested in a perfect mapping.
Instead, we are interested in the approach you take in producing a repeatable
and accessible method of translating the data, probably in the form of a script.

Use any language that you consider to be appropriate.
Please do not use a tool such as Talend or Excel where the resulting process is hidden in
a proprietary format.

Please upload the resulting scripts into a github.com repository; feel free to include
multiple commits.

The entire exercise should take one to two hours.

Target Format
=============

The Darwin Core format can be viewed at https://dwc.tdwg.org/terms/
It is, largely, a flat format with a single, denormalised row expected for each record.
(There are ways of introducing more structure into DwC data but they are not relevant
for this exercise.)

The output can be any readily accessible file format; we recommend UTF-8 encoded CSV.

Not all DwC terms need to be present in the output.

The downstream ALA processing systems are capable of sorting out things like
translation from DMS latitudes and longitudes into decimal values or from northings
and eastings into latitude/longitude.
Similarly, most date forms and variants of vocabulary terms are handled.
If you find yourself doing sophisticated spherical mathematics or complex translation, you
have gone too far.

The one exception is dates.
Dates are prone to misinterpretation due to national vagaries.
Dates or date ranges should, therefore be translated into ISO 8601 form based on the assumption
that the origin is Australia or New Zealand.

Occurrence
----------

An occurrence record represents a sighting of an animal or plant.
At its base is who-when-where-what with terms drawn from all DwC classes,
including individualCount, recordedBy, eventDate or year/month/etc, decimal or verbatim lat/long and  scientificName.

There are terms in the source data that are not covered by DwC.
These should be included in the output.
These should simply be placed in suitable output columns, rather than added via
the http://rs.tdwg.org/dwc/terms/dynamicProperties term or MeasurementOrFact class.

Dataset
=======

SA Flora Sample.csv is a sample of the occurrence records supplied by the
South Australian government.

The DATEACCURACY column gives the range of possible dates that the record
may have been taken on.
Most of these are self-explanatory but T means decade.

The SPRELIBCODE is the level of identification verification, with
Y for verified and P for pending.

The NSXCODE is the taxon identifier for the suppliers own internal taxonomic
database and can be discarded.

Questions?
==========

Contact the ARGA Project Lead Software Engineer, Dr Nick dos Remedios (nick.dosremedios@csiro.au), if you have any questions about the intricacies of Darwin Core or the source data.
