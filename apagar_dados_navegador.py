import os
import shutil

# Definir caminho para a pasta principal de cookies
pasta_cookies = os.path.join(os.getcwd(), r'C:\Cookie')

def limpar_dados_desnecessarios(perfil_path):
    # print(f'Limpeza iniciada para o perfil: {perfil_path}')
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

    # Pastas internas da pasta Default que podem ser removidas
    pastas_default_para_remover = [
        'Cache', 'Code Cache', 'GPUCache', 'DawnWebGPUCache',
        'ShaderCache', 'DawnGraphiteCache', 'Download Service',
        'Feature Engagement Tracker', 'Safe Browsing Network',
        'Extension Rules', 'Extension State', 'Extension Scripts',
        'File System', 'blob_storage', 'WebStorage'
    ]

    # Remover pastas principais
    for pasta in pastas_para_remover:
        caminho_completo = os.path.join(perfil_path, pasta)
        if os.path.exists(caminho_completo):
            try:
                shutil.rmtree(caminho_completo)
                # print(f"Pasta '{pasta}' removida.")
            except Exception as e:
                print(f"Erro ao remover '{pasta}': {e}")

    # Remover pastas dentro de 'Default'
    default_path = os.path.join(perfil_path, 'Default')
    for pasta in pastas_default_para_remover:
        caminho_completo = os.path.join(default_path, pasta)
        if os.path.exists(caminho_completo):
            try:
                shutil.rmtree(caminho_completo)
                # print(f"Pasta '{pasta}' dentro de 'Default' removida.")
            except Exception as e:
                print(f"Erro ao remover '{pasta}' dentro de 'Default': {e}")

def limpar_todos_perfis():
    # Listar todas as subpastas na pasta principal de cookies
    if os.path.exists(pasta_cookies):
        for pasta_usuario in os.listdir(pasta_cookies):
            caminho_usuario = os.path.join(pasta_cookies, pasta_usuario)
            if os.path.isdir(caminho_usuario):
                limpar_dados_desnecessarios(caminho_usuario)
    else:
        print(f"A pasta '{pasta_cookies}' não existe.")



# Limpar dados desnecessários de todos os perfis
# limpar_todos_perfis()
