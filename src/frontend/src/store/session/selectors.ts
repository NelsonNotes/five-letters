import { TSessionState } from '../../types/session'
import { RootState } from '../types'

export const selectSession = (state: RootState): TSessionState => state.session
