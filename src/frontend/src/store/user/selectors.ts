import { TUserState } from '../../types/user'
import { RootState } from '../types'

export const selectUser = (state: RootState): TUserState => state.user
