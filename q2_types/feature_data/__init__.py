# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import (
    TaxonomyFormat, TaxonomyDirectoryFormat, HeaderlessTSVTaxonomyFormat,
    HeaderlessTSVTaxonomyDirectoryFormat, TSVTaxonomyFormat,
    TSVTaxonomyDirectoryFormat, DNAFASTAFormat, DNASequencesDirectoryFormat,
    PairedDNASequencesDirectoryFormat, AlignedDNAFASTAFormat,
    AlignedDNASequencesDirectoryFormat)
from ._type import (
    FeatureData, Taxonomy, Sequence, PairedEndSequence, AlignedSequence)

# TODO remove these imports when tests are rewritten. Remove from __all__ too
from ._transformer import DNAIterator, PairedDNAIterator, AlignedDNAIterator

__all__ = [
    'TaxonomyFormat', 'TaxonomyDirectoryFormat', 'HeaderlessTSVTaxonomyFormat',
    'HeaderlessTSVTaxonomyDirectoryFormat', 'TSVTaxonomyFormat',
    'TSVTaxonomyDirectoryFormat', 'DNAFASTAFormat',
    'DNASequencesDirectoryFormat', 'PairedDNASequencesDirectoryFormat',
    'AlignedDNAFASTAFormat', 'AlignedDNASequencesDirectoryFormat',
    'FeatureData', 'Taxonomy', 'Sequence', 'PairedEndSequence',
    'AlignedSequence', 'DNAIterator', 'PairedDNAIterator',
    'AlignedDNAIterator']

importlib.import_module('q2_types.feature_data._transformer')
