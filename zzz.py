import os
import shutil


def limpar_dados_desnecessarios(perfil_path):
    print('limpar_dados_desnecessarios')
    # Pastas principais para remover
    pastas_para_remover = [
        'GrShaderCache', 'ShaderCache', 'component_cnx_cache',
        'Crashpad', 'BrowserMetrics', 'CrashpadMetrics-active',
        'MediaFoundationWidevineCdm', 'OnDeviceHeadSuggestModel',
        'Subresource Filter', 'ThirdPartyModuleList64', 'OptimizationHints',
        'Crowd Deny', 'FileTypePolicies', 'FirstPartySetsPreloaded',
        'GraphiteDawnCache', 'hyphen-data', 'optimization_guide_model_store',
        'component_crx_cache',
    ]
    """ pasta que não podem ser apagadas
    Network
    """
    # Pastas internas da pasta Default que podem ser removidas
    pastas_default_para_remover = [
        'Cache', 'Code Cache', 'GPUCache', 'DawnWebGPUCache',
        'ShaderCache', 'DawnGraphiteCache', 'Download Service',
        'Feature Engagement Tracker', 'Safe Browsing Network',
        'Extension Rules', 'Extension State', 'Extension Scripts',
        'File System', 'blob_storage','WebStorage'
    ]

    # Remover pastas principais
    for pasta in pastas_para_remover:
        caminho_completo = os.path.join(perfil_path, pasta)
        if os.path.exists(caminho_completo):
            try:
                shutil.rmtree(caminho_completo)
                print(f"Pasta '{pasta}' removida.")
            except Exception as e:
                print(f"Erro ao remover '{pasta}': {e}")

    # Remover pastas dentro de 'Default'
    default_path = os.path.join(perfil_path, 'Default')
    for pasta in pastas_default_para_remover:
        caminho_completo = os.path.join(default_path, pasta)
        if os.path.exists(caminho_completo):
            try:
                shutil.rmtree(caminho_completo)
                print(f"Pasta '{pasta}' dentro de 'Default' removida.")
            except Exception as e:
                print(f"Erro ao remover '{pasta}' dentro de 'Default': {e}")


# Definir caminho para o perfil:
pasta_cookies = os.path.join(os.getcwd(), r'C:\Cookie')
id_conta = "61557294840037"  # Substitua pelo ID da conta desejada
perfil = os.path.join(pasta_cookies, str(id_conta))

# Chamar função para limpar dados desnecessários:
limpar_dados_desnecessarios(perfil)