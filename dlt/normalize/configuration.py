from typing import Type

from dlt.common.typing import StrAny
from dlt.common.data_writers import TLoaderFileFormat
from dlt.common.configuration import (PoolRunnerConfiguration, NormalizeVolumeConfiguration,
                                              LoadVolumeConfiguration, SchemaVolumeConfiguration,
                                              ProductionLoadVolumeConfiguration, ProductionNormalizeVolumeConfiguration,
                                              ProductionSchemaVolumeConfiguration,
                                              TPoolType, make_configuration)

from . import __version__


class NormalizeConfiguration(PoolRunnerConfiguration, NormalizeVolumeConfiguration, LoadVolumeConfiguration, SchemaVolumeConfiguration):
    LOADER_FILE_FORMAT: TLoaderFileFormat = "jsonl"  # jsonp or insert commands will be generated
    POOL_TYPE: TPoolType = "process"


class ProductionNormalizeConfiguration(ProductionNormalizeVolumeConfiguration, ProductionLoadVolumeConfiguration,
                                      ProductionSchemaVolumeConfiguration, NormalizeConfiguration):
    pass


def configuration(initial_values: StrAny = None) -> Type[NormalizeConfiguration]:
    return make_configuration(NormalizeConfiguration, ProductionNormalizeConfiguration, initial_values=initial_values)