# Sets up env för Kapp och SecretGen Controller installation - startas med <. ./rmqSetEnv.sh>
# Then you start the installation
# </> cd $HOME/tanzu-cluster-essentials </>
# </> ./install.sh --yes </>

export INSTALL_BUNDLE=registry.tanzu.vmware.com/tanzu-cluster-essentials/cluster-essentials-bundle@sha256:2354688e46d4bb4060f74fca069513c9b42ffa17a0a6d5b0dbb81ed52242ea44
export INSTALL_REGISTRY_HOSTNAME=registry.tanzu.vmware.com
export INSTALL_REGISTRY_USERNAME=msoderberg@vmware.com
export INSTALL_REGISTRY_PASSWORD=Th3darkhalf!
